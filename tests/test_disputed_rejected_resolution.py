import importlib.util
import os
import re
import unittest
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "mapex_health_check.py"

os.environ.setdefault("JIRA_BASE_URL", "https://tomtom.atlassian.net")
os.environ.setdefault("JIRA_EMAIL", "test@example.com")
os.environ.setdefault("JIRA_API_TOKEN", "token")
os.environ.setdefault("CONFLUENCE_PARENT_PAGE_ID", "1")

spec = importlib.util.spec_from_file_location("mapex_health_check", MODULE_PATH)
mapex_health_check = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(mapex_health_check)

REJECTED_TAG = "[REJECTED]"
POTENTIAL_TAG = "[POTENTIAL DISPUTE]"

# Column indices of the disputed table
COL_KEY = 0
COL_CLASSIFICATION = 1
COL_SUMMARY = 2
COL_RESOLUTION = 4
COL_SIGNAL = 7
COL_EVIDENCE = 8
COL_SEVERITY = 9
COL_MANUAL_VALIDATION = 10
COL_VALIDATION_NOTES = 11
NUM_COLUMNS = 12


class DisputedRejectedResolutionTests(unittest.TestCase):
    def make_issue(self, key="MAPEX-200", **field_overrides):
        fields = {
            "summary": "Synthetic rejected test issue",
            "status": {"name": "Closed", "statusCategory": {"key": "done"}},
            "resolution": {"name": "Rejected"},
            "resolutiondate": "2026-10-01T12:00:00.000+0000",
            "reporter": {"accountId": "reporter-1", "displayName": "Reporter One"},
            "assignee": {"displayName": "Assignee One"},
            "comment": {"comments": []},
            "created": "2026-08-01T00:00:00.000+0000",
            "updated": "2026-10-05T00:00:00.000+0000",
            "duedate": None,
        }
        fields.update(field_overrides)
        return {"key": key, "fields": fields}

    def comment(self, body, author_id="reporter-1", created="2026-10-02T00:00:00.000+0000"):
        return {
            "body": body,
            "created": created,
            "author": {"accountId": author_id, "displayName": author_id},
        }

    def table_rows(self, section):
        header_seen = False
        rows = []
        for line in section.splitlines():
            if line.startswith("| Key |"):
                header_seen = True
                continue
            if not header_seen or not line.startswith("|"):
                continue
            if re.match(r"^\|[\s\-|:]+\|$", line):
                continue
            rows.append(mapex_health_check._split_table_row(line))
        return rows

    # -- Detection -----------------------------------------------------------

    def test_rejected_resolution_without_comments_is_flagged(self):
        issue = self.make_issue()
        signals, evidence = mapex_health_check.detect_disputed_signals(issue, set())
        self.assertEqual(signals, ["Rejected resolution"])
        self.assertEqual(evidence, ["Resolution set to Rejected"])
        self.assertEqual(mapex_health_check.severity_for_signals(signals), "High")
        self.assertEqual(mapex_health_check.classification_for_signals(signals), REJECTED_TAG)

        section, new_keys = mapex_health_check.build_disputed_section([issue], set())
        self.assertEqual(new_keys, ["MAPEX-200"])
        rows = self.table_rows(section)
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(len(row), NUM_COLUMNS)
        self.assertEqual(row[COL_KEY], "MAPEX-200")
        self.assertEqual(row[COL_CLASSIFICATION], REJECTED_TAG)
        self.assertEqual(row[COL_RESOLUTION], "Rejected")
        self.assertEqual(row[COL_SIGNAL], "Rejected resolution")
        self.assertEqual(row[COL_EVIDENCE], "Resolution set to Rejected")
        self.assertEqual(row[COL_SEVERITY], "High")
        self.assertEqual(row[COL_MANUAL_VALIDATION], "Pending review")
        self.assertEqual(row[COL_VALIDATION_NOTES], mapex_health_check.DEFAULT_VALIDATION_NOTES)

    def test_rejected_resolution_with_neutral_comments_is_flagged(self):
        issue = self.make_issue(
            comment={"comments": [
                self.comment("Thanks, noted.", author_id="assignee-1"),
                self.comment("FYI attached the screenshot.", author_id="other-1"),
            ]},
        )
        signals, evidence = mapex_health_check.detect_disputed_signals(issue, set())
        self.assertEqual(signals, ["Rejected resolution"])
        self.assertEqual(evidence, ["Resolution set to Rejected"])

    def test_rejected_resolution_case_insensitive_and_trimmed(self):
        for name in ("rejected", "REJECTED", "  Rejected  ", "\tReJeCtEd\n"):
            with self.subTest(resolution=name):
                issue = self.make_issue(resolution={"name": name})
                signals, evidence = mapex_health_check.detect_disputed_signals(issue, set())
                self.assertEqual(signals, ["Rejected resolution"])
                self.assertEqual(evidence, ["Resolution set to Rejected"])
                self.assertEqual(
                    mapex_health_check.classification_for_signals(signals), REJECTED_TAG
                )

    def test_rejected_plus_other_signals_single_row_with_all_evidence(self):
        issue = self.make_issue(
            "MAPEX-MULTI",
            status={"name": "Open", "statusCategory": {"key": "new"}},
            comment={"comments": [
                self.comment("This is wrong, please redo.", author_id="client-1"),
            ]},
        )
        issue["changelog"] = {
            "histories": [
                {"items": [{"field": "status", "fromString": "Closed", "toString": "Open"}]}
            ]
        }
        signals, evidence = mapex_health_check.detect_disputed_signals(issue, set())
        self.assertEqual(
            signals,
            ["Rejected resolution", "Reopened after closure", "Dissatisfaction keyword in comment"],
        )
        self.assertEqual(mapex_health_check.severity_for_signals(signals), "High")

        section, new_keys = mapex_health_check.build_disputed_section([issue], set())
        self.assertEqual(new_keys, ["MAPEX-MULTI"])
        rows = self.table_rows(section)
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(len(row), NUM_COLUMNS)
        self.assertEqual(row[COL_CLASSIFICATION], REJECTED_TAG)
        self.assertIn("Rejected resolution", row[COL_SIGNAL])
        self.assertIn("Reopened after closure", row[COL_SIGNAL])
        self.assertIn("Dissatisfaction keyword in comment", row[COL_SIGNAL])
        self.assertIn("Resolution set to Rejected", row[COL_EVIDENCE])
        self.assertIn("Status WAS Closed, now reopened", row[COL_EVIDENCE])
        self.assertIn("Comment by client-1", row[COL_EVIDENCE])
        self.assertEqual(row[COL_SEVERITY], "High")
        self.assertEqual(row[COL_MANUAL_VALIDATION], "Pending review")

    def test_keyword_dispute_keeps_potential_dispute_tag(self):
        issue = self.make_issue(
            "MAPEX-KW",
            resolution={"name": "Done"},
            comment={"comments": [self.comment("This is wrong, please redo.", author_id="client-1")]},
        )
        signals, _ = mapex_health_check.detect_disputed_signals(issue, set())
        self.assertEqual(signals, ["Dissatisfaction keyword in comment"])
        self.assertEqual(mapex_health_check.classification_for_signals(signals), POTENTIAL_TAG)

        section, _ = mapex_health_check.build_disputed_section([issue], set())
        rows = self.table_rows(section)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][COL_CLASSIFICATION], POTENTIAL_TAG)
        self.assertEqual(rows[0][COL_SEVERITY], "High")
        self.assertEqual(rows[0][COL_MANUAL_VALIDATION], "Pending review")
        self.assertEqual(rows[0][COL_VALIDATION_NOTES], mapex_health_check.DEFAULT_VALIDATION_NOTES)

    def test_status_rejected_without_rejected_resolution_does_not_trigger(self):
        issue = self.make_issue(
            "MAPEX-STATUS",
            status={"name": "Rejected", "statusCategory": {"key": "done"}},
            resolution={"name": "Won't Do"},
        )
        signals, evidence = mapex_health_check.detect_disputed_signals(issue, set())
        self.assertEqual(signals, [])
        self.assertEqual(evidence, [])

    def test_historical_rejected_resolution_transition_does_not_trigger(self):
        issue = self.make_issue(
            "MAPEX-HIST",
            resolution={"name": "Won't Do"},
        )
        issue["changelog"] = {
            "histories": [
                {"items": [{"field": "resolution", "fromString": None, "toString": "Rejected"}]},
                {"items": [{"field": "resolution", "fromString": "Rejected", "toString": "Won't Do"}]},
            ]
        }
        signals, _ = mapex_health_check.detect_disputed_signals(issue, set())
        self.assertNotIn("Rejected resolution", signals)
        self.assertEqual(signals, [])

    def test_other_resolutions_without_signals_not_flagged(self):
        for res in (None, {"name": "Done"}, {"name": "Won't Do"}, {"name": "Duplicate"},
                    {"name": "Rejected by customer"}):
            with self.subTest(resolution=res):
                issue = self.make_issue("MAPEX-OTHER", resolution=res)
                signals, _ = mapex_health_check.detect_disputed_signals(issue, set())
                self.assertEqual(signals, [])
                section, new_keys = mapex_health_check.build_disputed_section([issue], set())
                self.assertEqual(new_keys, [])
                self.assertIn("_No new disputed tickets detected in this reporting period._", section)

    def test_excluded_comment_filtering_unchanged(self):
        excluded = {"excluded-account"}
        # Rejected still flagged even if all comments are from excluded authors,
        # but excluded keyword comments do not add keyword evidence.
        issue = self.make_issue(
            comment={"comments": [
                self.comment("This is wrong, please redo.", author_id="excluded-account"),
            ]},
        )
        signals, evidence = mapex_health_check.detect_disputed_signals(issue, excluded)
        self.assertEqual(signals, ["Rejected resolution"])
        self.assertEqual(evidence, ["Resolution set to Rejected"])

        # Non-rejected ticket with only excluded keyword comments is not flagged.
        done_issue = self.make_issue(
            "MAPEX-EXCL",
            resolution={"name": "Done"},
            comment={"comments": [
                self.comment("This is wrong, please redo.", author_id="excluded-account"),
            ]},
        )
        signals, _ = mapex_health_check.detect_disputed_signals(done_issue, excluded)
        self.assertEqual(signals, [])

        # Without exclusion the same comment is still a keyword signal.
        signals, _ = mapex_health_check.detect_disputed_signals(done_issue, set())
        self.assertEqual(signals, ["Dissatisfaction keyword in comment"])

    def test_history_suppression_preserved_for_rejected(self):
        issue = self.make_issue("MAPEX-SEEN")
        section, new_keys = mapex_health_check.build_disputed_section([issue], {"MAPEX-SEEN"})
        self.assertEqual(new_keys, [])
        self.assertNotIn("MAPEX-SEEN", section)

        report, report_keys = mapex_health_check.build_report(
            [issue], {"MAPEX-SEEN"}, date(2026, 10, 13)
        )
        self.assertEqual(report_keys, [])
        self.assertIn("_No new disputed tickets detected in this reporting period._", report)
        self.assertNotIn("| MAPEX-SEEN |", report)

    # -- Report --------------------------------------------------------------

    def test_report_keys_consistent_with_table(self):
        issues = [
            self.make_issue("MAPEX-301"),  # Rejected, no comments
            self.make_issue(
                "MAPEX-302",
                resolution={"name": "Done"},
                comment={"comments": [self.comment("This is wrong.", author_id="client-1")]},
            ),  # keyword dispute
            self.make_issue("MAPEX-303", resolution={"name": "Done"}),  # no signal
            self.make_issue("MAPEX-304"),  # Rejected but already in history
        ]
        report, new_keys = mapex_health_check.build_report(
            issues, {"MAPEX-304"}, date(2026, 10, 13)
        )
        self.assertEqual(sorted(new_keys), ["MAPEX-301", "MAPEX-302"])
        self.assertIn("| MAPEX-301 |", report)
        self.assertIn("| MAPEX-302 |", report)
        self.assertNotIn("| MAPEX-303 |", report)
        self.assertNotIn("| MAPEX-304 |", report)

        section, _ = mapex_health_check.build_disputed_section(issues, {"MAPEX-304"})
        rows = self.table_rows(section)
        self.assertEqual(len(rows), 2)
        tags = {r[COL_KEY]: r[COL_CLASSIFICATION] for r in rows}
        self.assertEqual(tags, {"MAPEX-301": REJECTED_TAG, "MAPEX-302": POTENTIAL_TAG})

    def test_legend_and_manual_validation_preserved(self):
        section, _ = mapex_health_check.build_disputed_section([self.make_issue()], set())
        self.assertIn("Classification legend", section)
        self.assertIn(REJECTED_TAG, section)
        self.assertIn(POTENTIAL_TAG, section)
        self.assertIn("current Jira resolution is recorded as Rejected", section)
        self.assertIn("not a completed human validation", section)
        self.assertIn("not Jira or Confluence labels", section)
        self.assertIn("Manual Review Instructions", section)
        self.assertIn("Manual Validation", section)
        self.assertIn("Validation Notes", section)

    def test_classification_renders_in_confluence_html(self):
        issue = self.make_issue(
            "MAPEX-HTML",
            summary="Rejected change at LA,Nevada|USA with | pipes\nand newline",
            status={"name": "Open", "statusCategory": {"key": "new"}},
            comment={"comments": [
                self.comment(
                    "This is wrong | pending updates\r\nthrough DB.",
                    author_id="client-1",
                ),
            ]},
        )
        section, _ = mapex_health_check.build_disputed_section([issue], set())
        html = mapex_health_check.markdown_to_confluence_storage(section)

        th_matches = re.findall(r"<th>(.*?)</th>", html)
        self.assertEqual(len(th_matches), NUM_COLUMNS)
        self.assertEqual(th_matches[COL_CLASSIFICATION], "Classification")

        tr_matches = re.findall(r"<tr>(.*?)</tr>", html, flags=re.DOTALL)
        row_html = next(tr for tr in tr_matches if "MAPEX-HTML" in tr)
        td_matches = re.findall(r"<td>(.*?)</td>", row_html, flags=re.DOTALL)
        self.assertEqual(len(td_matches), NUM_COLUMNS)
        self.assertEqual(td_matches[COL_CLASSIFICATION], REJECTED_TAG)
        self.assertIn("LA,Nevada|USA", td_matches[COL_SUMMARY])
        self.assertNotIn("\n", td_matches[COL_SUMMARY])
        self.assertIn("Resolution set to Rejected", td_matches[COL_EVIDENCE])
        self.assertIn("wrong | pending updates", td_matches[COL_EVIDENCE])
        self.assertEqual(td_matches[COL_MANUAL_VALIDATION], "Pending review")
        self.assertIn("to be filled", td_matches[COL_VALIDATION_NOTES])

        # Legend renders as list items without being turned into links.
        self.assertIn(f"<strong>{REJECTED_TAG}</strong>", html)
        self.assertIn(f"<strong>{POTENTIAL_TAG}</strong>", html)


if __name__ == "__main__":
    unittest.main()
