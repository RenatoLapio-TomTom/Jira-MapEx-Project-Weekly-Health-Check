import importlib.util
import os
import unittest
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


class ConfluenceLinkConversionTests(unittest.TestCase):
    def test_markdown_link_converts_to_anchor(self):
        text = "[MAPEX-9922](https://tomtom.atlassian.net/browse/MAPEX-9922)"
        rendered = mapex_health_check._md_inline(text)
        self.assertEqual(
            rendered,
            '<a href="https://tomtom.atlassian.net/browse/MAPEX-9922">MAPEX-9922</a>',
        )

    def test_plain_key_in_bold_is_linkified(self):
        rendered = mapex_health_check._md_inline("**MAPEX-9922**")
        self.assertEqual(
            rendered,
            '<strong><a href="https://tomtom.atlassian.net/browse/MAPEX-9922">MAPEX-9922</a></strong>',
        )

    def test_table_cells_convert_plain_mapex_key_to_link(self):
        markdown = "| Key |\n|-----|\n| MAPEX-9922 |"
        html = mapex_health_check.markdown_to_confluence_storage(markdown)
        self.assertIn(
            '<td><a href="https://tomtom.atlassian.net/browse/MAPEX-9922">MAPEX-9922</a></td>',
            html,
        )

    def test_list_items_convert_plain_mapex_key_to_link(self):
        markdown = "- MAPEX-9922"
        html = mapex_health_check.markdown_to_confluence_storage(markdown)
        self.assertIn(
            '<li><a href="https://tomtom.atlassian.net/browse/MAPEX-9922">MAPEX-9922</a></li>',
            html,
        )


if __name__ == "__main__":
    unittest.main()
