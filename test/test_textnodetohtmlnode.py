import unittest
from htmlnode import *

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_type_text(self):
        # Test conversion of a TextNode with TextType.TEXT to a LeafNode
        text_node = TextNode("Plain text", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Plain text")

    def test_text_type_bold(self):
        # Test conversion of a TextNode with TextType.BOLD to a LeafNode
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_text_type_italic(self):
        # Test conversion of a TextNode with TextType.ITALIC to a LeafNode
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_text_type_code(self):
        # Test conversion of a TextNode with TextType.CODE to a LeafNode
        text_node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Code text</code>")

    def test_text_type_link(self):
        # Test conversion of a TextNode with TextType.LINK to a LeafNode
        text_node = TextNode("Link text", TextType.LINK)
        text_node.url = "https://www.example.com"
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.example.com">Link text</a>')

    def test_text_type_image(self):
        # Test conversion of a TextNode with TextType.IMAGE to a LeafNode
        text_node = TextNode("Image alt text", TextType.IMAGE)
        text_node.url = "https://www.example.com/image.png"
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://www.example.com/image.png" alt="Image alt text"/>')

    def test_invalid_text_type(self):
        # Test that an invalid TextType raises an Exception
        text_node = TextNode("Invalid text", "INVALID")
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(text_node)
        self.assertEqual(str(context.exception), "Invalid TextType")

if __name__ == "__main__":
    unittest.main()