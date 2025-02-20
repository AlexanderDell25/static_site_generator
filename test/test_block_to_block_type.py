# filepath: /home/adell/workspace/github.com/AlexanderDell25/static_site_generator/src/test_blockmarkdown.py
import unittest
from blockmarkdown import markdown_to_blocks, block_to_block_type, BlockType

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

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        # Test identifying a heading block
        block = "# This is a heading"
        expected = BlockType.heading
        self.assertEqual(block_to_block_type(block), expected)

    def test_block_to_block_type_paragraph(self):
        # Test identifying a paragraph block
        block = "This is a paragraph of text."
        expected = BlockType.paragraph
        self.assertEqual(block_to_block_type(block), expected)

    def test_block_to_block_type_code(self):
        # Test identifying a code block
        block = "```This is a code block```"
        expected = BlockType.code
        self.assertEqual(block_to_block_type(block), expected)

    def test_block_to_block_type_quote(self):
        # Test identifying a quote block
        block = "> This is a quote"
        expected = BlockType.quote
        self.assertEqual(block_to_block_type(block), expected)

    def test_block_to_block_type_unordered_list(self):
        # Test identifying an unordered list block
        block = "* This is a list item"
        expected = BlockType.unordered_list
        self.assertEqual(block_to_block_type(block), expected)

    def test_block_to_block_type_ordered_list(self):
        # Test identifying an ordered list block
        block = "1. This is a list item"
        expected = BlockType.ordered_list
        self.assertEqual(block_to_block_type(block), expected)

if __name__ == "__main__":
    unittest.main()