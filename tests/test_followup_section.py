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


class FollowupSectionTests(unittest.TestCase):
    def test_followup_includes_only_high_risk_late_and_disputed(self) -> None:
        at_risk_rows = [
            {"key": "MAPEX-1", "assignee": "A", "risk_cat": "Open Overdue", "risk_lvl": "High"},
            {"key": "MAPEX-2", "assignee": "B", "risk_cat": "Open Overdue", "risk_lvl": "Medium"},
            {"key": "MAPEX-3", "assignee": "C", "risk_cat": "Closed Late", "risk_lvl": "High"},
        ]
        disputed_rows = [
            {"key": "MAPEX-4", "assignee": "D", "severity": "High"},
        ]

        section = health_check.build_followup_section(at_risk_rows, disputed_rows)
        self.assertIn("| MAPEX-1 |", section)
        self.assertIn("| MAPEX-4 |", section)
        self.assertNotIn("| MAPEX-2 |", section)
        self.assertNotIn("| MAPEX-3 |", section)

    def test_followup_merges_duplicate_key_reasons(self) -> None:
        at_risk_rows = [
            {"key": "MAPEX-10", "assignee": "Owner", "risk_cat": "Open Overdue", "risk_lvl": "Critical"},
        ]
        disputed_rows = [
            {"key": "MAPEX-10", "assignee": "Owner", "severity": "Medium"},
        ]

        section = health_check.build_followup_section(at_risk_rows, disputed_rows)
        self.assertIn("Open Overdue — Critical risk; Rejected/Disputed — Medium severity", section)


if __name__ == "__main__":
    unittest.main()
