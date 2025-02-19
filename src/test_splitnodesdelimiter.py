import unittest
from htmlnode import TextNode, TextType
from splitnodesdelimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_code_block(self):
        # Test splitting a TextNode with inline code delimited by backticks
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_bold_text(self):
        # Test splitting a TextNode with bold text delimited by double asterisks
        node = TextNode("This is **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_italic_text(self):
        # Test splitting a TextNode with italic text delimited by single asterisks
        node = TextNode("This is *italic* text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_no_split(self):
        # Test that a TextNode without the delimiter remains unchanged
        node = TextNode("This is plain text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [node]
        self.assertEqual(new_nodes, expected_nodes)

if __name__ == "__main__":
    unittest.main()