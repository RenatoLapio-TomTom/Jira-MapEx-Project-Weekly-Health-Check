# Jira MapEx Project Weekly Health Check

Automated weekly health check pipeline for the **MAPEX** Jira project.
Runs every Saturday, generates a Markdown report, and publishes it as a child page in a Confluence personal space.

---

## How it works

1. The GitHub Actions workflow (`.github/workflows/mapex-health-check.yml`) triggers every **Saturday at ~17:00 CET** (16:00 UTC; DST drift of ±1 h is acceptable).
2. The script (`scripts/mapex_health_check.py`) queries Jira for all MAPEX tickets created in the **last 90 days**, excluding tickets reported by the configured list of Map Expert account IDs.
3. It produces a Markdown health report with only two sections:
   - **Top 5 Urgent Tickets** — up to five Critical or High risk tickets, ordered by risk level and then days overdue, using the existing ticket eligibility rules.
   - **Rejected / Disputed Tickets** — automated rule-based candidates requiring human validation (current resolution Rejected, incomplete resolution, reopening, dissatisfaction keywords, reporter post-closure comment). Each row has a **Classification** tag (`[REJECTED]` or `[POTENTIAL DISPUTE]`) and two manual validation columns (**Manual Validation** and **Validation Notes**) for team review in Confluence.
4. The report is:
   - Saved locally in `reports/mapex-health-YYYY-MM-DD.md` and committed back to the repository.
   - Published as a **child page** under `CONFLUENCE_PARENT_PAGE_ID` in `CONFLUENCE_SPACE_KEY`.
   - Uses the base page title `Jira MapEx Project Health Check Report - YYYY-MM-DD` first. If that title already exists in the target space, tries `_v1`, `_v2`, and so on, creating the first available title without overwriting existing pages.
5. Disputed ticket keys are persisted in `data/disputed_history.json` so they are **not re-reported** in future runs.

---

## Required GitHub Secrets

Add the following secrets under **Settings → Secrets and variables → Actions** in this repository:

| Secret | Description |
|--------|-------------|
| `JIRA_BASE_URL` | Jira instance URL, e.g. `https://tomtom.atlassian.net` |
| `JIRA_EMAIL` | Atlassian account email |
| `JIRA_API_TOKEN` | Atlassian API token (generate at https://id.atlassian.com/manage-profile/security/api-tokens) |
| `CONFLUENCE_BASE_URL` | Confluence URL, e.g. `https://tomtom.atlassian.net/wiki` |
| `CONFLUENCE_EMAIL` | Atlassian account email (usually same as `JIRA_EMAIL`) |
| `CONFLUENCE_API_TOKEN` | Atlassian API token (can be same as `JIRA_API_TOKEN`) |
| `CONFLUENCE_SPACE_KEY` | Confluence space key, e.g. `~lapio` for personal space |
| `CONFLUENCE_PARENT_PAGE_ID` | Numeric ID of the parent page under which reports will be created |

### Optional environment variables (set in workflow or script defaults)

| Variable | Default | Description |
|----------|---------|-------------|
| `JIRA_PROJECT_KEY` | `MAPEX` | Jira project key to analyze |
| `LOOKBACK_DAYS` | `90` | Number of days to look back for ticket creation |

---

## Files

```
.github/
  workflows/
    mapex-health-check.yml   # GitHub Actions workflow
config/
  excluded_reporters.txt     # Jira accountIds excluded as ticket reporters and comment authors
data/
  disputed_history.json      # Persisted list of previously reported disputed ticket keys
reports/
  mapex-health-YYYY-MM-DD.md # Generated health reports (auto-committed each run)
scripts/
  mapex_health_check.py      # Main health check script
```

---

## Manual run

Trigger manually via **Actions → MAPEX Jira Weekly Health Check → Run workflow** in the GitHub UI, or using the GitHub CLI:

```bash
gh workflow run mapex-health-check.yml
```

---

## Disputed ticket history

`data/disputed_history.json` contains all ticket keys ever reported in the _Rejected / Disputed Tickets_ section.
Tickets in this list are suppressed from future reports.
To reset history (e.g., to force re-reporting), clear the `reported_keys` array in that file and commit.

Account IDs in `config/excluded_reporters.txt` exclude tickets when they are the reporter, and their comments are ignored for comment-based disputed signals (dissatisfaction keywords and reporter post-closure comments). A ticket can still be flagged by an independent signal, such as a Rejected or Incomplete resolution or reopening, or by qualifying comments from other authors.

---

## Manual Validation of Disputed Tickets

### Purpose and Candidate Nature
Tickets appearing in the **Rejected / Disputed Tickets** section are **automated rule-based candidates requiring human review**—they are not AI verdicts or confirmed rejections.

Detection relies on objective rules (any one signal is enough to flag a ticket):
- Current resolution set to **Rejected** (signal `Rejected resolution`, evidence `Resolution set to Rejected`, severity **High**) — flagged even with no comments, only neutral comments, or only comments from excluded authors
- Resolution set to **Incomplete**
- Ticket status **reopened after closure**
- Dissatisfaction or rework keywords detected in comments
- Any non-excluded comment posted by the reporter after closure when resolution is **Done**

Because the post-closure comment rule flags any reporter activity after resolution without analyzing sentiment or context, informational updates, administrative handover notes, or polite follow-up messages may be flagged as candidate disputes and can be false positives.

### Classification tags
The disputed table includes a **Classification** column with report-only tags (they are not Jira labels or Confluence page labels):

| Tag | Meaning |
|-----|---------|
| `[REJECTED]` | The ticket's **current** Jira resolution is recorded as Rejected (case-insensitive, whitespace-trimmed). This is a resolution value recorded in Jira, not a completed human validation. |
| `[POTENTIAL DISPUTE]` | Flagged solely by the other automated signals above; requires human validation. |

If a Rejected-resolution ticket also matches other signals, `[REJECTED]` takes precedence and the ticket stays a single row that keeps all evidence. Both classifications start as `Pending review` with the default validation notes placeholder.

Scope of the Rejected rule:
- Only the **current resolution** is checked. A historical resolution transition to Rejected, or a workflow **status** named Rejected, does not by itself trigger this signal.
- The existing limits still apply unchanged: only tickets created in the last `LOOKBACK_DAYS` (default 90) are analyzed, tickets reported by accounts in `config/excluded_reporters.txt` are excluded, and keys already in `data/disputed_history.json` are not re-reported.
- Rejected candidates appear in the **Rejected / Disputed Tickets** table; no executive-summary counts or RAG indicators are generated.

### Confluence Manual Review Instructions
Every newly generated disputed ticket row includes two validation columns:
- **Manual Validation** (defaults to `Pending review`)
- **Validation Notes** (defaults to `_(to be filled: reason, reviewer, date)_`)

These columns are **plain editable table cells** (not interactive dropdowns or macros). Any team member with Confluence page edit permissions can edit the published page to:
1. Update **Manual Validation** to **Confirmed dispute**, **False positive**, or leave as **Pending review**.
2. Fill in **Validation Notes** with the rationale/evidence, reviewer name, and review date (e.g., `False positive: informational DB update note | J. Doe, 2026-10-14`).

### Operational Scope and Limitations
- **Future pages only:** The validation columns are added to newly generated weekly health check pages going forward. Previously generated and published Confluence pages are not migrated or modified.
- **One-way publishing (no ingestion):** The automation publishes a new dated child page each week and does not read back or ingest edits made in Confluence. Manual validation is a lightweight review table for human visibility and auditability.
- **Report scope:** New reports contain only **Top 5 Urgent Tickets** and **Rejected / Disputed Tickets**. Manual edits in Confluence do not alter future automated detection runs.
- **Dispute history suppression:** Persisted keys in `data/disputed_history.json` continue to suppress tickets from being re-reported in subsequent runs regardless of human validation outcomes. Review states are not carried forward to subsequent weekly runs.
