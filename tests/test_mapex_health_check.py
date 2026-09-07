import importlib
import os
import sys
import unittest


class MdInlineMapexLinkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        os.environ.setdefault("JIRA_BASE_URL", "https://tomtom.atlassian.net")
        os.environ.setdefault("JIRA_EMAIL", "test@example.com")
        os.environ.setdefault("JIRA_API_TOKEN", "token")
        os.environ.setdefault("CONFLUENCE_PARENT_PAGE_ID", "1")

        if "scripts.mapex_health_check" in sys.modules:
            del sys.modules["scripts.mapex_health_check"]
        cls.module = importlib.import_module("scripts.mapex_health_check")

    def test_plain_mapex_key_is_linked(self) -> None:
        rendered = self.module._md_inline("Check MAPEX-9922 for details")
        self.assertIn(
            '<a href="https://tomtom.atlassian.net/browse/MAPEX-9922">MAPEX-9922</a>',
            rendered,
        )

    def test_existing_markdown_link_is_not_double_wrapped(self) -> None:
        rendered = self.module._md_inline("[MAPEX-9922](https://example.com/ticket)")
        self.assertEqual('<a href="https://example.com/ticket">MAPEX-9922</a>', rendered)

    def test_inline_code_mapex_key_is_not_linked(self) -> None:
        rendered = self.module._md_inline("`MAPEX-9922`")
        self.assertEqual("<code>MAPEX-9922</code>", rendered)


if __name__ == "__main__":
    unittest.main()
