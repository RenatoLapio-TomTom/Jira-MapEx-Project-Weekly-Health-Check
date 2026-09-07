import os
import sys
import unittest
from pathlib import Path


os.environ.setdefault("JIRA_BASE_URL", "https://example.atlassian.net")
os.environ.setdefault("JIRA_EMAIL", "test@example.com")
os.environ.setdefault("JIRA_API_TOKEN", "token")
os.environ.setdefault("CONFLUENCE_PARENT_PAGE_ID", "12345")

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import mapex_health_check as health_check


class DisputedDetectionTests(unittest.TestCase):
    def _issue_with_comment(self, body: str) -> dict:
        return {
            "key": "MAPEX-1",
            "fields": {
                "resolution": {"name": "Done"},
                "resolutiondate": "2026-09-01T00:00:00.000+0000",
                "status": {"name": "Done", "statusCategory": {"key": "done"}},
                "reporter": {"accountId": "reporter-1"},
                "comment": {
                    "comments": [
                        {
                            "body": body,
                            "author": {"accountId": "external-1", "displayName": "External User"},
                            "created": "2026-08-31T00:00:00.000+0000",
                        }
                    ]
                },
            },
            "changelog": {"histories": []},
        }

    def test_technical_wrong_comment_not_flagged(self) -> None:
        body = (
            "Thank you for the quick turnaround. I first reported this metric as 0.9796. "
            "That was wrong — it came from a local run. Much appreciated."
        )
        signals, _ = health_check.detect_disputed_signals(self._issue_with_comment(body))
        self.assertNotIn("Dissatisfaction keyword in comment", signals)

    def test_appreciative_comment_with_keyword_not_flagged(self) -> None:
        body = (
            "Thanks for the update. The earlier number was incorrect, but now everything is fixed. "
            "No further questions from me, so please go ahead and close."
        )
        signals, _ = health_check.detect_disputed_signals(self._issue_with_comment(body))
        self.assertNotIn("Dissatisfaction keyword in comment", signals)

    def test_rejection_comment_still_flagged(self) -> None:
        body = "This does not meet requirements. Please rework and reopen."
        signals, _ = health_check.detect_disputed_signals(self._issue_with_comment(body))
        self.assertIn("Dissatisfaction keyword in comment", signals)

    def test_false_positive_regex_matches_wrong_but_pattern(self) -> None:
        body = "I first shared an earlier value. That was wrong — but this is corrected in CI."
        self.assertIsNotNone(health_check.FALSE_POSITIVE_CONTEXTS.search(body))


if __name__ == "__main__":
    unittest.main()
