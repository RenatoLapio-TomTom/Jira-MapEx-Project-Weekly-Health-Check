import importlib.util
import os
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import requests


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


class ConfluencePublishingTests(unittest.TestCase):
    def response(self, results):
        response = Mock()
        response.json.return_value = {"results": results}
        return response

    def publish_with_existing_titles(self, existing_titles, expected_title):
        base_title = "Weekly Report"
        seen_titles = []

        def lookup(url, **kwargs):
            self.assertEqual(url, f"{mapex_health_check.CONFLUENCE_BASE_URL}/rest/api/content")
            params = kwargs["params"]
            self.assertEqual(params["spaceKey"], mapex_health_check.CONFLUENCE_SPACE_KEY)
            self.assertEqual(params["type"], "page")
            self.assertEqual(params["status"], "current")
            seen_titles.append(params["title"])
            return self.response([{"id": "10"}] if params["title"] in existing_titles else [])

        published = Mock(ok=True)
        published.json.return_value = {"_links": {"webui": "/spaces/test/pages/20"}}
        with patch.object(mapex_health_check.requests, "get", side_effect=lookup), \
             patch.object(mapex_health_check.requests, "post", return_value=published) as post:
            mapex_health_check.publish_to_confluence(base_title, "## Report")

        post.assert_called_once()
        payload = post.call_args.kwargs["json"]
        self.assertEqual(payload["title"], expected_title)
        self.assertEqual(payload["ancestors"], [{"id": mapex_health_check.CONFLUENCE_PARENT_PAGE_ID}])
        self.assertEqual(payload["space"], {"key": mapex_health_check.CONFLUENCE_SPACE_KEY})
        self.assertEqual(payload["body"]["storage"]["value"], "<h2>Report</h2>")
        return seen_titles

    def test_available_base_title_is_used(self):
        self.assertEqual(self.publish_with_existing_titles(set(), "Weekly Report"), ["Weekly Report"])

    def test_existing_base_title_uses_v1(self):
        self.assertEqual(
            self.publish_with_existing_titles({"Weekly Report"}, "Weekly Report_v1"),
            ["Weekly Report", "Weekly Report_v1"],
        )

    def test_existing_versions_are_checked_sequentially(self):
        self.assertEqual(
            self.publish_with_existing_titles(
                {"Weekly Report", "Weekly Report_v1", "Weekly Report_v2"}, "Weekly Report_v3"
            ),
            ["Weekly Report", "Weekly Report_v1", "Weekly Report_v2", "Weekly Report_v3"],
        )

    def test_first_available_version_is_used_even_with_later_versions(self):
        self.publish_with_existing_titles({"Weekly Report", "Weekly Report_v2"}, "Weekly Report_v1")

    def test_lookup_failure_does_not_create_page(self):
        response = Mock()
        response.raise_for_status.side_effect = requests.HTTPError("Lookup failed")
        with patch.object(mapex_health_check.requests, "get", return_value=response), \
             patch.object(mapex_health_check.requests, "post") as post:
            with self.assertRaises(requests.HTTPError):
                mapex_health_check.publish_to_confluence("Weekly Report", "Report")
        post.assert_not_called()

    def test_publish_failure_is_not_retried_under_another_title(self):
        failed = Mock(ok=False, status_code=403, text="Forbidden")
        with patch.object(mapex_health_check.requests, "get", return_value=self.response([])), \
             patch.object(mapex_health_check.requests, "post", return_value=failed) as post:
            with self.assertRaises(SystemExit):
                mapex_health_check.publish_to_confluence("Weekly Report", "Report")
        post.assert_called_once()


if __name__ == "__main__":
    unittest.main()
