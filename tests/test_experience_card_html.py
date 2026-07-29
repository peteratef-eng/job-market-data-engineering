from __future__ import annotations

import unittest

from portfolio.content.experience import EXPERIENCE
from ui.components import _experience_card_html


class ExperienceCardHtmlTest(unittest.TestCase):
    def test_card_html_renders_as_html_not_markdown_code(self) -> None:
        card_html = _experience_card_html(EXPERIENCE[0], class_name="experience-hover-card")

        self.assertTrue(card_html.lstrip().startswith("<article"))
        self.assertIn('<ul class="experience-list">', card_html)
        self.assertIn("<li>", card_html)
        self.assertIn('<span class="meta-pill">', card_html)
        self.assertNotIn("```", card_html)
        self.assertNotIn("<pre>", card_html)
        self.assertNotIn("<code>", card_html)

        for line in card_html.splitlines():
            if line.strip():
                self.assertFalse(line.startswith("    "), repr(line))


if __name__ == "__main__":
    unittest.main()
