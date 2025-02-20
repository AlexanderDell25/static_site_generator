import unittest
from blockmarkdown import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_empty_text(self):
        # Test converting empty text
        markdown = ""
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_markdown_to_blocks_single_block(self):
        # Test converting single block of text
        markdown = "This is a single block of text."
        expected = ["This is a single block of text."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_markdown_to_blocks_multiple_blocks(self):
        # Test converting multiple blocks of text
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_markdown_to_blocks_excessive_newlines(self):
        # Test converting text with excessive newlines
        markdown = "# This is a heading\n\n\n\nThis is a paragraph of text.\n\n\n\n* This is a list item"
        expected = [
            "# This is a heading",
            "This is a paragraph of text.",
            "* This is a list item"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_markdown_to_blocks_leading_trailing_whitespace(self):
        # Test converting text with leading and trailing whitespace
        markdown = "  # This is a heading  \n\n  This is a paragraph of text.  \n\n  * This is a list item  "
        expected = [
            "# This is a heading",
            "This is a paragraph of text.",
            "* This is a list item"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

if __name__ == "__main__":
    unittest.main()