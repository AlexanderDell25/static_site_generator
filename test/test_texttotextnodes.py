import unittest
from textnode import TextNode, TextType
from splitnodesdelimiter import *

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_text_nodes_empty_text(self):
        # Test converting empty text
        text = ""
        expected = [TextNode("", TextType.TEXT)]
        self.assertEqual(text_to_text_nodes(text), expected)

    def test_text_to_text_nodes_plain_text(self):
        # Test converting plain text with no markdown
        text = "This is plain text."
        expected = [TextNode("This is plain text.", TextType.TEXT)]
        self.assertEqual(text_to_text_nodes(text), expected)

    def test_text_to_text_nodes_bold_text(self):
        # Test converting text with bold markdown
        text = "This is **bold** text."
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(text_to_text_nodes(text), expected)

    def test_text_to_text_nodes_italic_text(self):
        # Test converting text with italic markdown
        text = "This is *italic* text."
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(text_to_text_nodes(text), expected)

    def test_text_to_text_nodes_code_block(self):
        # Test converting text with code block markdown
        text = "This is `code` text."
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(text_to_text_nodes(text), expected)

    def test_text_to_text_nodes_image(self):
        # Test converting text with image markdown
        text = "This is an ![image](https://example.com/image.png)."
        expected = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(text_to_text_nodes(text), expected)

    def test_text_to_text_nodes_link(self):
        # Test converting text with link markdown
        text = "This is a [link](https://example.com)."
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(text_to_text_nodes(text), expected)

if __name__ == "__main__":
    unittest.main()