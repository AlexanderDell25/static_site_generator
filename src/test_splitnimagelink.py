import unittest
from htmlnode import TextNode, TextType
from splitnodesimagelink import split_nodes_image, split_nodes_link

class TestSplitNodesImageLink(unittest.TestCase):
    def test_split_nodes_image_empty_text(self):
        # Test splitting images from empty text
        node = TextNode("", TextType.TEXT)
        expected = [node]
        self.assertEqual(split_nodes_image([node]), expected)

    def test_split_nodes_link_empty_text(self):
        # Test splitting links from empty text
        node = TextNode("", TextType.TEXT)
        expected = [node]
        self.assertEqual(split_nodes_link([node]), expected)

    def test_split_nodes_image_no_images(self):
        # Test splitting images from text with no images
        node = TextNode("This is text with no images.", TextType.TEXT)
        expected = [node]
        self.assertEqual(split_nodes_image([node]), expected)

    def test_split_nodes_link_no_links(self):
        # Test splitting links from text with no links
        node = TextNode("This is text with no links.", TextType.TEXT)
        expected = [node]
        self.assertEqual(split_nodes_link([node]), expected)

    def test_split_nodes_link_multiple_links(self):
        # Test splitting multiple links from text
        node = TextNode("This is a link [to example 1](https://example.com/1) and [to example 2](https://example.com/2)", TextType.TEXT)
        expected = [
            TextNode("This is a link ", TextType.TEXT),
            TextNode("to example 1", TextType.LINK, "https://example.com/1"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to example 2", TextType.LINK, "https://example.com/2"),
        ]
        self.assertEqual(split_nodes_link([node]), expected)

    def test_split_nodes_non_text_node(self):
        node = "NonTextNode"
        expected = [node]
        self.assertEqual(split_nodes_image([node]), expected)
        self.assertEqual(split_nodes_link([node]), expected)

    
if __name__ == "__main__":
    unittest.main()