import importlib.util
import os
import unittest
from datetime import date
from pathlib import Path
import re


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


class DisputedManualValidationTests(unittest.TestCase):
    def make_issue(self, key="MAPEX-100", **field_overrides):
        fields = {
            "summary": "Synthetic test issue",
            "status": {"name": "Closed", "statusCategory": {"key": "done"}},
            "resolution": {"name": "Done"},
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

    def test_disputed_table_headers_and_defaults(self):
        issue = self.make_issue(
            comment={"comments": [self.comment("Hi, informational follow-up note after Done.")]}
        )
        section, new_keys = mapex_health_check.build_disputed_section([issue], set())

        self.assertEqual(new_keys, ["MAPEX-100"])
        self.assertIn("## 2. Rejected / Disputed Tickets", section)

        header_line = next(line for line in section.splitlines() if line.startswith("| Key |"))
        headers = [c.strip() for c in header_line.strip("|").split("|")]
        self.assertEqual(
            headers,
            [
                "Key",
                "Classification",
                "Summary",
                "Status",
                "Resolution",
                "Reporter",
                "Assignee",
                "Signal",
                "Evidence",
                "Severity",
                "Manual Validation",
                "Validation Notes",
            ],
        )

        data_lines = [
            line for line in section.splitlines()
            if line.startswith("| MAPEX-100 |")
        ]
        self.assertEqual(len(data_lines), 1)
        row = mapex_health_check._split_table_row(data_lines[0])
        self.assertEqual(len(row), 12)
        self.assertEqual(row[0], "MAPEX-100")
        self.assertEqual(row[1], "[POTENTIAL DISPUTE]")
        self.assertEqual(row[10], "Pending review")
        self.assertEqual(row[11], mapex_health_check.DEFAULT_VALIDATION_NOTES)

    def test_manual_review_guidance_text_in_disputed_section(self):
        issue = self.make_issue(
            comment={"comments": [self.comment("Post-resolution comment")]}
        )
        section, _ = mapex_health_check.build_disputed_section([issue], set())

        self.assertIn("automated rule-based candidates requiring human validation", section)
        self.assertIn("not AI verdicts or confirmed rejections", section)
        self.assertIn("Confirmed dispute", section)
        self.assertIn("False positive", section)
        self.assertIn("Pending review", section)
        self.assertIn("Manual Validation", section)
        self.assertIn("Validation Notes", section)
        self.assertIn("plain editable table cells", section)
        self.assertIn("not interactive dropdowns", section)
        self.assertIn("reporter after closure", section)
        self.assertIn("false positives", section)

    def test_empty_disputed_section_behavior(self):
        issue = self.make_issue()  # No signals
        section, new_keys = mapex_health_check.build_disputed_section([issue], set())

        self.assertEqual(new_keys, [])
        self.assertIn("## 2. Rejected / Disputed Tickets", section)
        self.assertIn("_No new disputed tickets detected in this reporting period._", section)
        self.assertNotIn("| Key |", section)

    def test_unchanged_automated_signals_evidence_severity_and_exclusion(self):
        # 1. Incomplete resolution -> High
        inc_issue = self.make_issue("MAPEX-INC", resolution={"name": "Incomplete"})
        signals, evidence = mapex_health_check.detect_disputed_signals(inc_issue, set())
        self.assertEqual(signals, ["Incomplete resolution"])
        self.assertEqual(evidence, ["Resolution set to Incomplete"])
        self.assertEqual(mapex_health_check.severity_for_signals(signals), "High")

        # 2. Reopened -> Medium
        reopened_issue = self.make_issue(
            "MAPEX-REOPEN",
            status={"name": "Open", "statusCategory": {"key": "new"}},
        )
        reopened_issue["changelog"] = {
            "histories": [
                {"items": [{"field": "status", "fromString": "Closed", "toString": "Open"}]}
            ]
        }
        signals, evidence = mapex_health_check.detect_disputed_signals(reopened_issue, set())
        self.assertEqual(signals, ["Reopened after closure"])
        self.assertEqual(evidence, ["Status WAS Closed, now reopened"])
        self.assertEqual(mapex_health_check.severity_for_signals(signals), "Medium")

        # 3. Dissatisfaction keyword -> High
        kw_issue = self.make_issue(
            "MAPEX-KW",
            comment={"comments": [self.comment("This is wrong, please redo.", author_id="client-1")]},
        )
        signals, evidence = mapex_health_check.detect_disputed_signals(kw_issue, set())
        self.assertEqual(signals, ["Dissatisfaction keyword in comment"])
        self.assertIn("wrong", evidence[0])
        self.assertEqual(mapex_health_check.severity_for_signals(signals), "High")

        # 4. Reporter comment after resolution -> Low
        post_issue = self.make_issue(
            "MAPEX-POST",
            comment={"comments": [self.comment("Thanks for the fix.", author_id="reporter-1")]},
        )
        signals, evidence = mapex_health_check.detect_disputed_signals(post_issue, set())
        self.assertEqual(signals, ["Reporter commented after closure"])
        self.assertIn("Reporter comment after resolution", evidence[0])
        self.assertEqual(mapex_health_check.severity_for_signals(signals), "Low")

        # 5. Excluded reporter comment ignored
        excluded_set = {"reporter-1"}
        signals, evidence = mapex_health_check.detect_disputed_signals(post_issue, excluded_set)
        self.assertEqual(signals, [])
        self.assertEqual(evidence, [])

    def test_spurious_columns_prevention_with_literal_pipes_and_multi_signal_evidence(self):
        # Create issue with:
        # - literal pipe in summary
        # - multiple signals (Incomplete resolution + dissatisfaction keyword comment containing pipe and newline)
        issue = self.make_issue(
            "MAPEX-PIPE",
            summary="Restriction changes at LA,Nevada|USA with | pipes\nand newline",
            resolution={"name": "Incomplete"},
            comment={"comments": [
                self.comment(
                    "This is wrong | pending updates | will be redo\r\nthrough DB. Kind regards",
                    author_id="reporter-1",
                    created="2026-10-03T00:00:00.000+0000",
                )
            ]},
        )
        # Verify detect_disputed_signals returns both evidence items
        signals, evidence = mapex_health_check.detect_disputed_signals(issue, set())
        self.assertEqual(len(signals), 2)
        self.assertEqual(len(evidence), 2)

        section, new_keys = mapex_health_check.build_disputed_section([issue], set())
        self.assertEqual(new_keys, ["MAPEX-PIPE"])

        # Check Confluence HTML storage conversion
        html = mapex_health_check.markdown_to_confluence_storage(section)

        # Count th in the header
        th_matches = re.findall(r"<th>(.*?)</th>", html)
        self.assertEqual(len(th_matches), 12)

        # Count td in the row
        tr_matches = re.findall(r"<tr>(.*?)</tr>", html, flags=re.DOTALL)
        self.assertTrue(len(tr_matches) >= 1)
        # Find the row corresponding to MAPEX-PIPE
        pipe_row = next(tr for tr in tr_matches if "MAPEX-PIPE" in tr)
        td_matches = re.findall(r"<td>(.*?)</td>", pipe_row, flags=re.DOTALL)
        self.assertEqual(len(td_matches), 12)
        self.assertEqual(td_matches[1], "[POTENTIAL DISPUTE]")

        # Ensure literal pipes are preserved inside cells without creating extra columns
        summary_cell = td_matches[2]
        self.assertIn("LA,Nevada|USA", summary_cell)

        evidence_cell = td_matches[8]
        self.assertIn("Resolution set to Incomplete", evidence_cell)
        self.assertIn("Comment by reporter-1", evidence_cell)
        self.assertIn("wrong | pending updates", evidence_cell)

        validation_cell = td_matches[10]
        self.assertEqual(validation_cell, "Pending review")

        notes_cell = td_matches[11]
        self.assertIn("to be filled", notes_cell)

    def test_report_contains_only_requested_sections_and_review_notes(self):
        issue = self.make_issue(
            "MAPEX-100",
            comment={"comments": [self.comment("Thanks!")]},
        )
        report, _ = mapex_health_check.build_report([issue], set(), date(2026, 10, 13))

        self.assertEqual(
            re.findall(r"^## .+$", report, re.MULTILINE),
            ["## 1. Top 5 Urgent Tickets", "## 2. Rejected / Disputed Tickets"],
        )
        for removed in (
            "Executive Summary", "Overall Health", "Schedule Health",
            "Assignee Overload", "Recommendations", "At-Risk / Late Tickets", "Follow-up",
        ):
            self.assertNotIn(removed, report)
        self.assertIn("No urgent tickets at this time.", report)
        self.assertIn("automated rule-based candidates", report)
        self.assertIn("do not feed back into future automated detection runs", report)
        self.assertIn("Manual Validation", report)
        self.assertIn("Validation Notes", report)

    def test_urgent_ranking_and_five_ticket_limit_preserved(self):
        rows = [
            {
                "key": f"MAPEX-{i}", "summary": f"Urgent {i}", "risk_lvl": risk,
                "days_overdue": days, "risk_cat": "Open Overdue",
            }
            for i, (risk, days) in enumerate([
                ("High", 80), ("Critical", 100), ("High", 60),
                ("Critical", 120), ("High", 70), ("High", 50), ("Medium", 200),
            ])
        ]
        section = mapex_health_check.build_urgent_section(rows)
        self.assertEqual(
            re.findall(r"\*\*(MAPEX-\d+)\*\*", section),
            ["MAPEX-3", "MAPEX-1", "MAPEX-0", "MAPEX-4", "MAPEX-2"],
        )
        self.assertIn("120d overdue", section)

    def test_escape_table_cell_helper(self):
        self.assertEqual(mapex_health_check._escape_table_cell(None), "")
        self.assertEqual(mapex_health_check._escape_table_cell("Simple text"), "Simple text")
        self.assertEqual(
            mapex_health_check._escape_table_cell("Text with | pipe"),
            r"Text with \| pipe",
        )
        self.assertEqual(
            mapex_health_check._escape_table_cell(r"Text with \| already escaped"),
            r"Text with \| already escaped",
        )
        self.assertEqual(
            mapex_health_check._escape_table_cell("Line 1\r\nLine 2\nLine 3\rLine 4"),
            "Line 1 Line 2 Line 3 Line 4",
        )


if __name__ == "__main__":
    unittest.main()
