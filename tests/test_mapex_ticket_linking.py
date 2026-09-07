import importlib
import os
import unittest


os.environ.setdefault("JIRA_BASE_URL", "https://tomtom.atlassian.net")
os.environ.setdefault("JIRA_EMAIL", "test@example.com")
os.environ.setdefault("JIRA_API_TOKEN", "test-token")
os.environ.setdefault("CONFLUENCE_PARENT_PAGE_ID", "1")

module = importlib.import_module("scripts.mapex_health_check")


class MapexTicketLinkingTests(unittest.TestCase):
    def test_plain_ticket_key_is_linkified(self) -> None:
        result = module.linkify_mapex_ticket_keys("MAPEX-9922")
        self.assertEqual(
            result,
            "[MAPEX-9922](https://tomtom.atlassian.net/browse/MAPEX-9922)",
        )

    def test_existing_markdown_link_is_not_double_wrapped(self) -> None:
        text = "[MAPEX-9922](https://tomtom.atlassian.net/browse/MAPEX-9922)"
        result = module.linkify_mapex_ticket_keys(text)
        self.assertEqual(result, text)

    def test_key_inside_browse_url_is_not_modified(self) -> None:
        text = "https://tomtom.atlassian.net/browse/MAPEX-9922"
        result = module.linkify_mapex_ticket_keys(text)
        self.assertEqual(result, text)


if __name__ == "__main__":
    unittest.main()
