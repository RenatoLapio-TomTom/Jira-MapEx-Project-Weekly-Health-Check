#!/usr/bin/env python3
"""
MAPEX Jira Project Weekly Health Check
Generates a Markdown health report and publishes it to Confluence.
"""

from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import requests
from dateutil import parser as dateutil_parser
from requests.auth import HTTPBasicAuth

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
EXCLUDED_REPORTERS_FILE = REPO_ROOT / "config" / "excluded_reporters.txt"
DISPUTED_HISTORY_FILE = REPO_ROOT / "data" / "disputed_history.json"

JIRA_BASE_URL = os.environ["JIRA_BASE_URL"].rstrip("/")
JIRA_EMAIL = os.environ["JIRA_EMAIL"]
JIRA_API_TOKEN = os.environ["JIRA_API_TOKEN"]

CONFLUENCE_BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "https://tomtom.atlassian.net/wiki").rstrip("/")
CONFLUENCE_EMAIL = os.environ.get("CONFLUENCE_EMAIL", JIRA_EMAIL)
CONFLUENCE_API_TOKEN = os.environ.get("CONFLUENCE_API_TOKEN", JIRA_API_TOKEN)
CONFLUENCE_SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY", "~lapio")
CONFLUENCE_PARENT_PAGE_ID = os.environ["CONFLUENCE_PARENT_PAGE_ID"]

PROJECT_KEY = os.environ.get("JIRA_PROJECT_KEY", "MAPEX")
LOOKBACK_DAYS = int(os.environ.get("LOOKBACK_DAYS", "90"))

TODAY = date.today()
TODAY_DT = datetime.combine(TODAY, datetime.min.time(), tzinfo=timezone.utc)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_excluded_reporters() -> set[str]:
    lines = EXCLUDED_REPORTERS_FILE.read_text().splitlines()
    return {l.strip() for l in lines if l.strip() and not l.strip().startswith("#")}


def load_disputed_history() -> set[str]:
    if DISPUTED_HISTORY_FILE.exists():
        data = json.loads(DISPUTED_HISTORY_FILE.read_text())
        return set(data.get("reported_keys", []))
    return set()


def save_disputed_history(keys: set[str]) -> None:
    DISPUTED_HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    existing = load_disputed_history()
    merged = sorted(existing | keys)
    DISPUTED_HISTORY_FILE.write_text(json.dumps({"reported_keys": merged}, indent=2) + "\n")


def jira_auth() -> HTTPBasicAuth:
    return HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)


def confluence_auth() -> HTTPBasicAuth:
    return HTTPBasicAuth(CONFLUENCE_EMAIL, CONFLUENCE_API_TOKEN)
    
def jira_get(path: str, params: dict | None = None) -> dict:
    url = f"{JIRA_BASE_URL}/rest/api/3{path}"
    resp = requests.get(
        url,
        auth=jira_auth(),
        params=params,
        headers={"Accept": "application/json"},
        timeout=60,
    )
    if not resp.ok:
        print(f"[ERROR] Jira GET {path} -> {resp.status_code}: {resp.text}", file=sys.stderr)
    resp.raise_for_status()
    return resp.json()

def parse_date(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return dateutil_parser.parse(value).date()
    except Exception:
        return None


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        dt = dateutil_parser.parse(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        return None


def days_between(a: date, b: date) -> int:
    return (a - b).days


# ---------------------------------------------------------------------------
# Jira API
# ---------------------------------------------------------------------------

def jira_post(path: str, json_body: dict) -> dict:
    url = f"{JIRA_BASE_URL}/rest/api/3{path}"
    resp = requests.post(
        url,
        auth=jira_auth(),
        json=json_body,
        headers={"Accept": "application/json", "Content-Type": "application/json"},
        timeout=60,
    )
    if not resp.ok:
        print(f"[ERROR] Jira POST {path} -> {resp.status_code}: {resp.text}", file=sys.stderr)
    resp.raise_for_status()
    return resp.json()


def jira_search(jql: str, fields: list[str], expand: list[str] | None = None) -> list[dict]:
    """Search Jira issues via /rest/api/3/search/jql with token-based pagination."""
    issues: list[dict] = []
    next_page_token: str | None = None
    max_results = 100

    while True:
        params = {
            "jql": jql,
            "fields": ",".join(fields),
            "maxResults": max_results,
        }
        if expand:
            params["expand"] = ",".join(expand)
        if next_page_token:
            params["nextPageToken"] = next_page_token

        data = jira_get("/search/jql", params=params)

        batch = data.get("issues") or data.get("values") or []
        is_last = bool(data.get("isLast", True))
        next_page_token = data.get("nextPageToken")

        print(
            f"[DEBUG] jira_search batch={len(batch)} "
            f"isLast={is_last} nextPageToken={'yes' if next_page_token else 'no'}"
        )

        issues.extend(batch)

        if is_last or not batch:
            break

    return issues



def fetch_changelog(issue_key: str) -> list[dict]:
    """Fetch all changelog entries for an issue."""
    histories: list[dict] = []
    start_at = 0
    while True:
        data = jira_get(f"/issue/{issue_key}/changelog", params={"startAt": start_at, "maxResults": 100})
        values = data.get("values", [])
        histories.extend(values)
        total = data.get("total", 0)
        start_at += len(values)
        if start_at >= total or not values:
            break
    return histories


# ---------------------------------------------------------------------------
# Data collection
# ---------------------------------------------------------------------------

FIELDS = [
    "summary", "status", "resolution", "resolutiondate",
    "created", "updated", "duedate", "assignee", "reporter",
    "priority", "comment", "issuetype",
]


def collect_issues(excluded_reporter_ids: set[str]) -> list[dict]:
    fields = [
        "summary", "status", "resolution", "resolutiondate",
        "created", "updated", "duedate", "assignee", "reporter",
        "priority", "comment", "issuetype"
    ]
    expand = ["changelog"]

    jql = f'project = "{PROJECT_KEY}" AND created >= -{LOOKBACK_DAYS}d ORDER BY created DESC'
    print(f"[INFO] JQL: {jql}")
    raw = jira_search(jql, fields=fields, expand=expand)
    print(f"[INFO] Raw issues fetched: {len(raw)}")

    filtered: list[dict] = []
    excluded_count = 0
    missing_reporter_id = 0

    for issue in raw:
        reporter = ((issue.get("fields") or {}).get("reporter") or {})
        rid = reporter.get("accountId")
        if not rid:
            missing_reporter_id += 1
        if rid in excluded_reporter_ids:
            excluded_count += 1
            continue
        filtered.append(issue)

    print(f"[INFO] Excluded by reporter list: {excluded_count}")
    print(f"[INFO] Missing reporter accountId: {missing_reporter_id}")
    print(f"[INFO] Issues after exclusion: {len(filtered)}")
    return filtered

# ---------------------------------------------------------------------------
# Analysis helpers
# ---------------------------------------------------------------------------

REJECTION_KEYWORDS = re.compile(
    r"\breject(ed|ion)?\b|\bnot acceptable\b|\bincorrect\b|\bwrong\b"
    r"|\bredo\b|\brework\b|\breopen\b|\bunsatisfied\b|\bdoes not meet\b",
    re.IGNORECASE,
)

FALSE_POSITIVE_CONTEXTS = re.compile(
    r"\bno(t)? wrong\b|\bcorrect(ly)?\b|\bwas correct\b|\blooks good\b"
    r"|\bseems (fine|ok|correct)\b|\breview (is )?(complete|done|approved)\b",
    re.IGNORECASE,
)


def get_field(issue: dict, *keys: str) -> Any:
    obj = issue.get("fields", {})
    for k in keys:
        if obj is None:
            return None
        obj = obj.get(k)
    return obj


def status_name(issue: dict) -> str:
    return (get_field(issue, "status", "name") or "").strip()


def status_category(issue: dict) -> str:
    return (get_field(issue, "status", "statusCategory", "key") or "").strip()


def resolution_name(issue: dict) -> str:
    return (get_field(issue, "resolution", "name") or "").strip()


def assignee_name(issue: dict) -> str:
    a = get_field(issue, "assignee")
    if not a:
        return ""
    return a.get("displayName") or a.get("name") or ""


def reporter_name(issue: dict) -> str:
    r = get_field(issue, "reporter")
    if not r:
        return ""
    return r.get("displayName") or r.get("name") or ""


def priority_name(issue: dict) -> str:
    return (get_field(issue, "priority", "name") or "").strip()


def issue_key(issue: dict) -> str:
    return issue.get("key", "")


def issue_summary(issue: dict) -> str:
    return (get_field(issue, "summary") or "").strip()


def due_date(issue: dict) -> date | None:
    return parse_date(get_field(issue, "duedate"))


def updated_date(issue: dict) -> date | None:
    return parse_date(get_field(issue, "updated"))


def resolution_date(issue: dict) -> date | None:
    return parse_date(get_field(issue, "resolutiondate"))


def created_date(issue: dict) -> date | None:
    return parse_date(get_field(issue, "created"))


def changelog_histories(issue: dict) -> list[dict]:
    return issue.get("changelog", {}).get("histories", [])


def was_closed_and_reopened(issue: dict) -> bool:
    """Return True if status was Closed at some point and current status is not Closed."""
    if status_name(issue).lower() == "closed":
        return False
    for history in changelog_histories(issue):
        for item in history.get("items", []):
            if item.get("field") == "status" and (item.get("fromString") or "").lower() == "closed":
                return True
    return False


def detect_disputed_signals(issue: dict) -> tuple[list[str], list[str]]:
    """Return (signals, evidence) lists for disputed detection."""
    signals: list[str] = []
    evidence: list[str] = []

    # Signal 1: resolution = Incomplete
    if resolution_name(issue).lower() == "incomplete":
        signals.append("Incomplete resolution")
        evidence.append("Resolution set to Incomplete")

    # Signal 2: was Closed but now open/other
    if was_closed_and_reopened(issue):
        signals.append("Reopened after closure")
        evidence.append("Status WAS Closed, now reopened")

    # Signal 3: keywords in comments
    comments = get_field(issue, "comment", "comments") or []
    for c in comments:
        body = c.get("body", "")
        if isinstance(body, dict):
            # Jira API v3 uses Atlassian Document Format
            body = _extract_adf_text(body)
        if REJECTION_KEYWORDS.search(body) and not FALSE_POSITIVE_CONTEXTS.search(body):
            author_id = (c.get("author") or {}).get("accountId", "")
            author_name = (c.get("author") or {}).get("displayName", author_id)
            snippet = body[:120].replace("\n", " ").strip()
            signals.append("Dissatisfaction keyword in comment")
            evidence.append(f'Comment by {author_name}: "{snippet}…"')
            break  # one evidence entry is enough

    # Signal 4: reporter commented after closure when resolution = Done
    if resolution_name(issue).lower() == "done":
        rd = resolution_date(issue)
        reporter_id = (get_field(issue, "reporter") or {}).get("accountId", "")
        comments = get_field(issue, "comment", "comments") or []
        for c in comments:
            c_author = (c.get("author") or {}).get("accountId", "")
            c_date = parse_date(c.get("created"))
            if c_author == reporter_id and c_date and rd and c_date > rd:
                body = c.get("body", "")
                if isinstance(body, dict):
                    body = _extract_adf_text(body)
                snippet = body[:120].replace("\n", " ").strip()
                signals.append("Reporter commented after closure")
                evidence.append(f'Reporter comment after resolution: "{snippet}…"')
                break

    return signals, evidence


def _extract_adf_text(node: Any, _depth: int = 0) -> str:
    """Extract plain text from Atlassian Document Format (ADF) JSON."""
    if isinstance(node, str):
        return node
    if isinstance(node, dict):
        parts: list[str] = []
        if node.get("type") == "text":
            parts.append(node.get("text", ""))
        for child in node.get("content", []):
            parts.append(_extract_adf_text(child, _depth + 1))
        return " ".join(p for p in parts if p)
    if isinstance(node, list):
        return " ".join(_extract_adf_text(n, _depth + 1) for n in node)
    return ""


def severity_for_signals(signals: list[str]) -> str:
    if not signals:
        return "Low"
    combined = " ".join(signals).lower()
    if "incomplete resolution" in combined or "dissatisfaction keyword" in combined:
        return "High"
    if "reopened" in combined or "rework" in combined:
        return "Medium"
    return "Low"


SEVERITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}
RISK_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}


def compute_risk_level(days_overdue: int | None, prio: str, risk_cat: str) -> str:
    if days_overdue is None:
        days_overdue = 0
    if days_overdue > 90 or (prio.lower() == "blocker" and days_overdue > 0):
        return "Critical"
    if 30 < days_overdue <= 90 or risk_cat == "Blocked":
        return "High"
    if 0 < days_overdue <= 30 or risk_cat in ("Due Soon – Not Started", "Closed Late"):
        return "Medium"
    return "Low"


# ---------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------

def build_disputed_section(issues: list[dict], history: set[str]) -> tuple[str, list[str]]:
    rows: list[dict] = []
    new_keys: list[str] = []

    for issue in issues:
        key = issue_key(issue)
        if key in history:
            continue
        signals, evidence = detect_disputed_signals(issue)
        if not signals:
            continue
        sev = severity_for_signals(signals)
        rows.append({
            "key": key,
            "summary": issue_summary(issue),
            "status": status_name(issue),
            "resolution": resolution_name(issue) or "—",
            "reporter": reporter_name(issue),
            "assignee": assignee_name(issue) or "—",
            "signal": "; ".join(set(signals)),
            "evidence": " | ".join(evidence[:2]),
            "severity": sev,
            "updated": updated_date(issue) or date.min,
        })
        new_keys.append(key)

    rows.sort(key=lambda r: (SEVERITY_ORDER.get(r["severity"], 99), -(r["updated"] - date.min).days))

    lines: list[str] = []
    lines.append("## 2. Rejected / Disputed Tickets\n")
    lines.append(
        "Tickets where work was potentially rejected or challenged, "
        "identified through resolution status, reopening history, comment keywords, "
        "or reporter post-closure activity.\n"
    )
    if not rows:
        lines.append("_No new disputed tickets detected in this reporting period._\n")
    else:
        lines.append("| Key | Summary | Status | Resolution | Reporter | Assignee | Signal | Evidence | Severity |")
        lines.append("|-----|---------|--------|------------|----------|----------|--------|----------|----------|")
        for r in rows:
            lines.append(
                f"| {r['key']} | {r['summary']} | {r['status']} | {r['resolution']} "
                f"| {r['reporter']} | {r['assignee']} | {r['signal']} | {r['evidence']} | {r['severity']} |"
            )
        lines.append("")
    return "\n".join(lines), new_keys


def build_at_risk_section(issues: list[dict]) -> tuple[str, list[dict]]:
    EXCLUDED_STATUSES = {"on hold", "blocked", "closed"}
    NOT_STARTED = {"backlog", "planned", "open"}

    seen: set[str] = set()
    rows: list[dict] = []

    def add(issue: dict, risk_cat: str, days_ov: int | None, closed_date_val: date | None = None, note: str = "") -> None:
        key = issue_key(issue)
        status = status_name(issue)
        if status.lower() in EXCLUDED_STATUSES:
            return
        if key in seen:
            return
        seen.add(key)
        prio = priority_name(issue)
        days_display = str(days_ov) if days_ov is not None else "n/a"
        risk_lvl = compute_risk_level(days_ov, prio, risk_cat)
        summary_text = issue_summary(issue)
        if note:
            summary_text = f"{summary_text} {note}"
        rows.append({
            "key": key,
            "summary": summary_text,
            "status": status,
            "due_date": due_date(issue),
            "closed_date": closed_date_val,
            "days_overdue": days_ov,
            "days_display": days_display,
            "assignee": assignee_name(issue) or "—",
            "priority": prio or "—",
            "risk_cat": risk_cat,
            "risk_lvl": risk_lvl,
        })

    for issue in issues:
        dd = due_date(issue)
        rd = resolution_date(issue)
        stat_cat = status_category(issue)
        stat = status_name(issue).lower()
        upd = updated_date(issue) or TODAY

        is_done = stat_cat == "done"
        is_excluded = stat in EXCLUDED_STATUSES

        # Open overdue
        if not is_done and not is_excluded and dd and dd < TODAY:
            add(issue, "Open Overdue", days_between(TODAY, dd))

        # Closed late
        if is_done and dd and rd:
            if rd > dd:
                add(issue, "Closed Late", days_between(rd, dd), closed_date_val=rd)
            elif not get_field(issue, "resolution"):
                add(issue, "Closed Late", days_between(rd, dd), closed_date_val=rd, note="⚠️ No resolution set")

        # Due soon, not started
        if not is_done and not is_excluded and dd and TODAY <= dd <= TODAY + __import__("datetime").timedelta(days=14):
            if stat in NOT_STARTED:
                add(issue, "Due Soon – Not Started", None)

        # Blocked with due date (for metric, but excluded from table per rules)
        # We include in at-risk table ONLY non-excluded, but Blocked is excluded status — skip here
        # (count is used in exec summary separately)

        # Stale
        if not is_done and not is_excluded and stat != "backlog":
            if dd is None and days_between(TODAY, upd) >= 30:
                add(issue, "Stale", None)

        # Unassigned with upcoming due date
        if not is_done and not is_excluded and dd and TODAY <= dd <= TODAY + __import__("datetime").timedelta(days=14):
            if not get_field(issue, "assignee"):
                add(issue, "Unassigned At-Risk", None)

    # Sort
    def sort_key(r: dict) -> tuple:
        rl = RISK_ORDER.get(r["risk_lvl"], 99)
        do = r["days_overdue"] if r["days_overdue"] is not None else -1
        return (rl, -do)

    rows.sort(key=sort_key)

    lines: list[str] = []
    lines.append("## 3. At-Risk / Late Tickets\n")
    lines.append(
        "Tickets that are overdue, blocked, stale, or at risk of missing their deadline. "
        "Tickets with status _On Hold_, _Blocked_, or _Closed_ are excluded from this table "
        "(though relevant metrics appear in the Executive Summary).\n"
    )
    if not rows:
        lines.append("_No at-risk tickets detected._\n")
    else:
        lines.append("| Key | Summary | Status | Due Date | Closed Date | Days Overdue | Assignee | Priority | Risk Category | Risk Level |")
        lines.append("|-----|---------|--------|----------|-------------|--------------|----------|----------|---------------|------------|")
        for r in rows:
            dd_str = str(r["due_date"]) if r["due_date"] else "—"
            cd_str = str(r["closed_date"]) if r["closed_date"] else "—"
            lines.append(
                f"| {r['key']} | {r['summary']} | {r['status']} | {dd_str} | {cd_str} "
                f"| {r['days_display']} | {r['assignee']} | {r['priority']} "
                f"| {r['risk_cat']} | {r['risk_lvl']} |"
            )
        lines.append("")
    return "\n".join(lines), rows


def build_followup_section(at_risk_rows: list[dict], disputed_rows_text: str) -> str:
    EXCLUDED_CATS = {"Due Soon – Not Started", "Closed Late"}
    rows = [r for r in at_risk_rows if r["risk_cat"] not in EXCLUDED_CATS]

    lines: list[str] = []
    lines.append("## 4. Follow-up\n")
    lines.append(
        "The table below lists all flagged tickets (excluding _Due Soon – Not Started_ and _Closed Late_ "
        "categories) that require follow-up action. Assignees are asked to review their tickets, "
        "provide a status update in the **Follow-up Status** column, and propose a recommendation "
        "in the **User Recommendation** column.\n"
    )
    lines.append(
        "**Why follow-up matters:** Timely follow-up on flagged tickets prevents recurring issues, "
        "supports continuous improvement, and ensures the project maintains healthy delivery rhythms. "
        "For the **User Recommendation** column, consider actions such as: adjusting the process that led "
        "to the delay, updating documentation, re-scoping the ticket, or escalating blockers.\n"
    )
    if not rows:
        lines.append("_No tickets require follow-up at this time._\n")
    else:
        lines.append("| Key | Assignee | Follow-up Status | Reason for Flagging | User Recommendation |")
        lines.append("|-----|----------|-----------------|---------------------|---------------------|")
        for r in rows:
            reason = f"{r['risk_cat']} — {r['risk_lvl']} risk"
            lines.append(f"| {r['key']} | {r['assignee']} | _(to be filled)_ | {reason} | _(to be filled)_ |")
        lines.append("")
    return "\n".join(lines)


def build_executive_summary(
    issues: list[dict],
    disputed_rows: list[dict],
    at_risk_rows: list[dict],
    report_date: date,
) -> str:
    since = TODAY_DT - __import__("datetime").timedelta(days=LOOKBACK_DAYS)
    since_date = since.date()

    total = len(issues)

    # Rejection rate
    total_closed = sum(1 for i in issues if status_category(i) == "done")
    flagged_disputed = len(disputed_rows)

    # Schedule health
    overdue_open = [r for r in at_risk_rows if r["risk_cat"] == "Open Overdue"]
    critical_count = sum(1 for r in overdue_open if r["risk_lvl"] == "Critical")
    high_count = sum(1 for r in overdue_open if r["risk_lvl"] == "High")

    # Blocked with due date (raw from issues, not filtered at-risk rows)
    blocked_with_due = [
        i for i in issues
        if status_name(i).lower() == "blocked" and due_date(i) is not None
    ]

    due_soon_not_started = [r for r in at_risk_rows if r["risk_cat"] == "Due Soon – Not Started"]
    stale_count = sum(1 for r in at_risk_rows if r["risk_cat"] == "Stale")

    # Top 5 urgent
    urgent = sorted(
        [r for r in at_risk_rows if r["risk_lvl"] in ("Critical", "High")],
        key=lambda r: (RISK_ORDER.get(r["risk_lvl"], 99), -(r["days_overdue"] or 0)),
    )[:5]

    # Assignee overload
    assignee_counts: Counter = Counter()
    for r in at_risk_rows:
        if r["assignee"] and r["assignee"] != "—":
            assignee_counts[r["assignee"]] += 1
    overloaded = {k: v for k, v in assignee_counts.items() if v >= 3}

    # RAG
    critical_total = sum(1 for r in at_risk_rows if r["risk_lvl"] == "Critical")
    high_total = sum(1 for r in at_risk_rows if r["risk_lvl"] == "High")
    if critical_total > 0:
        rag = "🔴"
    elif high_total >= 3 or flagged_disputed >= 5:
        rag = "🟡"
    else:
        rag = "🟢"

    # Build output
    lines: list[str] = []
    lines.append("## 1. Executive Summary\n")
    lines.append(f"**Overall Health:** {rag}\n")
    lines.append(
        f"**Scope:** {total} tickets analyzed | "
        f"{since_date} → {report_date} "
        '<span style="color:red"><strong>**Remark: only tickets created by Non-Map Experts are considered here*</strong></span>\n'
    )
    lines.append(
        f"**Rejection Rate:** {flagged_disputed} disputed/flagged vs {total_closed} total closed tickets in the last {LOOKBACK_DAYS} days\n"
    )
    lines.append("**Schedule Health:**\n")
    lines.append(f"- {len(overdue_open)} overdue ({critical_count} critical, {high_count} high)")
    lines.append(f"- {len(blocked_with_due)} blocked tickets with due dates")
    lines.append(f"- {len(due_soon_not_started)} due within 14 days, not started")
    lines.append(f"- {stale_count} stale (no update 30+ days)\n")

    lines.append("**Top 5 Urgent Tickets:**\n")
    if urgent:
        for r in urgent:
            days_str = f"{r['days_overdue']}d overdue" if r["days_overdue"] else r["risk_cat"]
            lines.append(f"- **{r['key']}** ({r['risk_lvl']}) — {r['summary']} [{days_str}]")
    else:
        lines.append("- _No urgent tickets at this time._")
    lines.append("")

    lines.append("**Assignee Overload (3+ flagged tickets):**\n")
    if overloaded:
        for name, count in sorted(overloaded.items(), key=lambda x: -x[1]):
            lines.append(f"- {name}: {count} flagged tickets")
    else:
        lines.append("- _No assignee overload detected._")
    lines.append("")

    lines.append("**Recommendations:**\n")
    if critical_count > 0:
        lines.append(f"1. 🔴 Immediately review and address {critical_count} critical overdue ticket(s) — these are >90 days late or blocker priority.")
    if len(blocked_with_due) > 0:
        lines.append(f"2. 🟡 Unblock {len(blocked_with_due)} ticket(s) that are blocked and have due dates to prevent further schedule slippage.")
    if stale_count > 0:
        lines.append(f"3. 🟡 Triage {stale_count} stale ticket(s) with no updates for 30+ days — close if obsolete or reassign/re-prioritize.")
    if not any([critical_count > 0, len(blocked_with_due) > 0, stale_count > 0]):
        lines.append("1. 🟢 Continue current delivery pace — no critical blockers detected.")
        lines.append("2. Monitor upcoming due dates to prevent future overruns.")
        lines.append("3. Review disputed tickets to improve ticket lifecycle quality.")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Report assembly
# ---------------------------------------------------------------------------

def build_report(issues: list[dict], history: set[str], report_date: date) -> tuple[str, list[str]]:
    print("[INFO] Building disputed section ...")
    disputed_text, new_disputed_keys = build_disputed_section(issues, history)

    # Re-parse rows for exec summary usage
    disputed_rows = []
    for issue in issues:
        key = issue_key(issue)
        if key in history:
            continue
        signals, _ = detect_disputed_signals(issue)
        if signals:
            disputed_rows.append({"key": key})

    print("[INFO] Building at-risk section ...")
    at_risk_text, at_risk_rows = build_at_risk_section(issues)

    print("[INFO] Building executive summary ...")
    exec_summary = build_executive_summary(issues, disputed_rows, at_risk_rows, report_date)

    print("[INFO] Building follow-up section ...")
    followup_text = build_followup_section(at_risk_rows, disputed_text)

    title = f"Jira MapEx Project Health Check Report - {report_date}"
    header = f"# {title}\n\n_Generated on {report_date} by automated GitHub Actions workflow._\n"
    report = "\n\n".join([header, exec_summary, disputed_text, at_risk_text, followup_text])
    return report, new_disputed_keys


# ---------------------------------------------------------------------------
# Confluence publishing
# ---------------------------------------------------------------------------

def markdown_to_confluence_storage(md: str) -> str:
    """
    Convert markdown to a Confluence storage-format HTML representation.
    This is a best-effort conversion; complex markdown may require further tuning.
    """
    import html as html_lib

    lines = md.splitlines()
    output: list[str] = []
    in_table = False
    header_done = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Headings
        if line.startswith("### "):
            if in_table:
                output.append("</tbody></table>")
                in_table = False
                header_done = False
            output.append(f"<h3>{_md_inline(line[4:])}</h3>")
            i += 1
            continue
        if line.startswith("## "):
            if in_table:
                output.append("</tbody></table>")
                in_table = False
                header_done = False
            output.append(f"<h2>{_md_inline(line[3:])}</h2>")
            i += 1
            continue
        if line.startswith("# "):
            if in_table:
                output.append("</tbody></table>")
                in_table = False
                header_done = False
            output.append(f"<h1>{_md_inline(line[2:])}</h1>")
            i += 1
            continue

        # Table rows
        if line.startswith("|"):
            # Skip separator rows
            if re.match(r"^\|[\s\-|:]+\|$", line):
                i += 1
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if not in_table:
                output.append('<table><thead><tr>')
                output.append("".join(f"<th>{_md_inline(c)}</th>" for c in cells))
                output.append("</tr></thead><tbody>")
                in_table = True
                header_done = True
            else:
                output.append("<tr>")
                output.append("".join(f"<td>{_md_inline(c)}</td>" for c in cells))
                output.append("</tr>")
            i += 1
            continue

        if in_table:
            output.append("</tbody></table>")
            in_table = False
            header_done = False

        # Bullet points
        if line.startswith("- ") or line.startswith("* "):
            # Collect list items
            list_lines = []
            while i < len(lines) and (lines[i].startswith("- ") or lines[i].startswith("* ")):
                list_lines.append(lines[i][2:])
                i += 1
            output.append("<ul>")
            for item in list_lines:
                output.append(f"<li>{_md_inline(item)}</li>")
            output.append("</ul>")
            continue

        # Numbered list
        nl_match = re.match(r"^(\d+)\. (.+)$", line)
        if nl_match:
            list_lines = []
            while i < len(lines) and re.match(r"^\d+\. .+$", lines[i]):
                m = re.match(r"^\d+\. (.+)$", lines[i])
                list_lines.append(m.group(1) if m else lines[i])
                i += 1
            output.append("<ol>")
            for item in list_lines:
                output.append(f"<li>{_md_inline(item)}</li>")
            output.append("</ol>")
            continue

        # Horizontal rule
        if re.match(r"^[-*_]{3,}$", line.strip()):
            output.append("<hr/>")
            i += 1
            continue

        # Blank line
        if not line.strip():
            output.append("<p></p>")
            i += 1
            continue

        # Paragraph
        output.append(f"<p>{_md_inline(line)}</p>")
        i += 1

    if in_table:
        output.append("</tbody></table>")

    return "\n".join(output)


def _md_inline(text: str) -> str:
    """Convert inline markdown (bold, italic, code, links) to HTML."""
    # Pass through raw HTML spans unchanged
    # Bold+italic
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", text)
    # Bold
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # Italic
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    # Inline code
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    # Links
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    # Emoji pass-through (they're unicode, fine in HTML)
    return text


def publish_to_confluence(title: str, content_md: str) -> None:
    storage_html = markdown_to_confluence_storage(content_md)
    payload = {
        "type": "page",
        "title": title,
        "ancestors": [{"id": CONFLUENCE_PARENT_PAGE_ID}],
        "space": {"key": CONFLUENCE_SPACE_KEY},
        "body": {
            "storage": {
                "value": storage_html,
                "representation": "storage",
            }
        },
    }
    url = f"{CONFLUENCE_BASE_URL}/rest/api/content"
    resp = requests.post(
        url,
        auth=confluence_auth(),
        json=payload,
        headers={"Content-Type": "application/json"},
        timeout=60,
    )
    if not resp.ok:
        print(f"[ERROR] Confluence publish failed: {resp.status_code}: {resp.text[:500]}", file=sys.stderr)
        sys.exit(1)
    page_url = resp.json().get("_links", {}).get("webui", "")
    print(f"[INFO] Published to Confluence: {CONFLUENCE_BASE_URL}{page_url}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"[INFO] MAPEX Health Check starting — report date {TODAY}")
    excluded = load_excluded_reporters()
    print(f"[INFO] Loaded {len(excluded)} excluded reporter account IDs")
    history = load_disputed_history()
    print(f"[INFO] Loaded {len(history)} previously reported disputed keys")

    issues = collect_issues(excluded)
    if not issues:
        print("[WARN] No issues found — check JQL / credentials.", file=sys.stderr)

    report_md, new_keys = build_report(issues, history, TODAY)

    # Save report locally
    reports_dir = REPO_ROOT / "reports"
    reports_dir.mkdir(exist_ok=True)
    report_path = reports_dir / f"mapex-health-{TODAY}.md"
    report_path.write_text(report_md)
    print(f"[INFO] Report saved: {report_path}")

    # Update history
    save_disputed_history(set(new_keys))
    print(f"[INFO] Disputed history updated with {len(new_keys)} new keys")

    # Publish to Confluence
    page_title = f"Jira MapEx Project Health Check Report - {TODAY}"
    print(f"[INFO] Publishing to Confluence as '{page_title}' ...")
    publish_to_confluence(page_title, report_md)
    print("[INFO] Done.")
