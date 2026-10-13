import importlib.util
import os
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


class DisputedCommentExclusionTests(unittest.TestCase):
    excluded = {"excluded-account"}

    def make_issue(self, **field_overrides):
        fields = {
            "summary": "Synthetic issue",
            "status": {"name": "Open", "statusCategory": {"key": "new"}},
            "resolution": None,
            "resolutiondate": None,
            "reporter": {"accountId": "reporter-account", "displayName": "Reporter"},
            "assignee": {"displayName": "Assignee"},
            "comment": {"comments": []},
            "created": "2026-01-01T00:00:00.000+0000",
            "updated": "2026-10-01T00:00:00.000+0000",
            "duedate": None,
        }
        fields.update(field_overrides)
        return {"key": "MAPEX-1", "fields": fields}

    def comment(self, body, author_id="allowed-account", created="2026-10-01"):
        comment = {"body": body, "created": created}
        if author_id is not None:
            comment["author"] = {"accountId": author_id, "displayName": author_id}
        return comment

    def detect(self, issue):
        return mapex_health_check.detect_disputed_signals(issue, self.excluded)

    def test_excluded_keyword_comment_does_not_flag_but_allowed_comment_does(self):
        issue = self.make_issue(comment={"comments": [self.comment("Please redo this", "excluded-account")]})
        self.assertEqual(self.detect(issue), ([], []))

        issue["fields"]["comment"]["comments"] = [self.comment("Please redo this")]
        signals, _ = self.detect(issue)
        self.assertIn("Dissatisfaction keyword in comment", signals)

    def test_excluded_matching_comment_does_not_hide_later_allowed_evidence(self):
        issue = self.make_issue(comment={"comments": [
            self.comment("Wrong, please rework", "excluded-account"),
            self.comment("This is incorrect", "allowed-account"),
        ]})
        signals, evidence = self.detect(issue)
        self.assertIn("Dissatisfaction keyword in comment", signals)
        self.assertIn("Comment by allowed-account", evidence[0])
        self.assertIn("incorrect", evidence[0])

    def test_excluded_comments_do_not_disable_independent_signals(self):
        comment = {"comments": [self.comment("Reject this", "excluded-account")]}
        incomplete = self.make_issue(
            resolution={"name": "Incomplete"},
            comment=comment,
        )
        signals, _ = self.detect(incomplete)
        self.assertEqual(signals, ["Incomplete resolution"])

        reopened = self.make_issue(
            comment=comment,
        )
        reopened["changelog"] = {"histories": [{"items": [
            {"field": "status", "fromString": "Closed", "toString": "Open"}
        ]}]}
        signals, _ = self.detect(reopened)
        self.assertEqual(signals, ["Reopened after closure"])

    def test_adf_comments_and_missing_author_ids_remain_safe_and_qualifying(self):
        adf_body = {"type": "doc", "content": [
            {"type": "paragraph", "content": [{"type": "text", "text": "Please redo this"}]}
        ]}
        issue = self.make_issue(comment={"comments": [
            self.comment(adf_body, "excluded-account"),
            {"body": "This is wrong", "author": {}},
        ]})
        signals, evidence = self.detect(issue)
        self.assertIn("Dissatisfaction keyword in comment", signals)
        self.assertIn("wrong", evidence[0])

        issue["fields"]["comment"]["comments"] = [{"body": "Please redo", "created": "2026-10-01"}]
        self.assertIn("Dissatisfaction keyword in comment", self.detect(issue)[0])

    def test_excluded_reporter_comment_after_resolution_is_ignored(self):
        issue = self.make_issue(
            resolution={"name": "Done"},
            resolutiondate="2026-09-01T00:00:00.000+0000",
            reporter={"accountId": "excluded-account", "displayName": "Reporter"},
            comment={"comments": [
                self.comment("Thanks", "excluded-account", "2026-09-02")
            ]},
        )
        self.assertEqual(self.detect(issue), ([], []))

        issue["fields"]["reporter"] = {
            "accountId": "reporter-account",
            "displayName": "Reporter",
        }
        issue["fields"]["comment"]["comments"] = [
            self.comment("Thanks", "reporter-account", "2026-09-02")
        ]
        self.assertIn("Reporter commented after closure", self.detect(issue)[0])

    def test_report_preserves_comment_exclusions(self):
        excluded_issue = self.make_issue(
            comment={"comments": [self.comment("Please redo this", "excluded-account")]}
        )
        excluded_issue["key"] = "MAPEX-1"
        allowed_issue = self.make_issue(
            comment={"comments": [self.comment("This is wrong", "allowed-account")]}
        )
        allowed_issue["key"] = "MAPEX-2"

        report, new_keys = mapex_health_check.build_report(
            [excluded_issue, allowed_issue], set(), date(2026, 10, 13), self.excluded
        )

        self.assertEqual(new_keys, ["MAPEX-2"])
        disputed_section = report.split("## 2. Rejected / Disputed Tickets", 1)[1]
        self.assertNotIn("| MAPEX-1 |", disputed_section)
        self.assertIn("| MAPEX-2 |", disputed_section)


if __name__ == "__main__":
    unittest.main()
