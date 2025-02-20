import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from blockmarkdown import *

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_markdown_to_html_node_empty_text(self):
        # Test converting empty text
        markdown = ""
        expected = ParentNode("div", [])
        self.assertEqual(markdown_to_html_node(markdown), expected)

    def test_markdown_to_html_node_heading(self):
        # Test converting a heading
        markdown = "# This is a heading"
        expected = ParentNode("div", [LeafNode("h1", "This is a heading")])
        self.assertEqual(markdown_to_html_node(markdown), expected)

    def test_markdown_to_html_node_paragraph(self):
        # Test converting a paragraph
        markdown = "This is a paragraph of text."
        expected = ParentNode("div", [ParentNode("p", [LeafNode(None, "This is a paragraph of text.")])])
        self.assertEqual(markdown_to_html_node(markdown), expected)

    def test_markdown_to_html_node_code(self):
        # Test converting a code block
        markdown = "```\nThis is a code block\n```"
        expected = ParentNode("div", [ParentNode("pre", [LeafNode("code", "This is a code block")])])
        self.assertEqual(markdown_to_html_node(markdown), expected)

    def test_markdown_to_html_node_quote(self):
        # Test converting a quote block
        markdown = "> This is a quote"
        expected = ParentNode("div", [ParentNode("blockquote", [LeafNode(None, "This is a quote")])])
        self.assertEqual(markdown_to_html_node(markdown), expected)

    def test_markdown_to_html_node_unordered_list(self):
        # Test converting an unordered list
        markdown = "* This is a list item\n* This is another list item"
        expected = ParentNode("div", [ParentNode("ul", [LeafNode("li", "This is a list item"), LeafNode("li", "This is another list item")])])
        self.assertEqual(markdown_to_html_node(markdown), expected)

    def test_markdown_to_html_node_ordered_list(self):
        # Test converting an ordered list
        markdown = "1. This is a list item\n2. This is another list item"
        expected = ParentNode("div", [ParentNode("ol", [LeafNode("li", "This is a list item"), LeafNode("li", "This is another list item")])])
        self.assertEqual(markdown_to_html_node(markdown), expected)

    def test_markdown_to_html_node_mixed(self):
        # Test converting mixed markdown
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected = ParentNode("div", [
            LeafNode("h1", "This is a heading"),
            ParentNode("p", [
                LeafNode(None, "This is a paragraph of text. It has some "),
                LeafNode("b", "bold"),
                LeafNode(None, " and "),
                LeafNode("i", "italic"),
                LeafNode(None, " words inside of it.")
            ]),
            ParentNode("ul", [
                LeafNode("li", "This is the first list item in a list block"),
                LeafNode("li", "This is a list item"),
                LeafNode("li", "This is another list item")
            ])
        ])
        self.assertEqual(markdown_to_html_node(markdown), expected)

if __name__ == "__main__":
    unittest.main()