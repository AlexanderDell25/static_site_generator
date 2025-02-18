import unittest
from htmlnode import *

class TestParentNode(unittest.TestCase):
    def test_no_tag(self):
        # Test that a ParentNode with no tag raises a ValueError
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "Child text")]).to_html()

    def test_no_children(self):
        # Test that a ParentNode with no children raises a ValueError
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

    def test_empty_children(self):
        # Test that a ParentNode with an empty children list raises a ValueError
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()

    def test_valid_tag_and_children(self):
        # Test that a ParentNode with a valid tag and children generates the correct HTML
        parent = ParentNode("div", [LeafNode("p", "Child text")])
        expected_html = "<div><p>Child text</p></div>"
        self.assertEqual(parent.to_html(), expected_html)

    def test_valid_tag_children_and_props(self):
        # Test that a ParentNode with a valid tag, children, and properties generates the correct HTML with properties
        parent = ParentNode("div", [LeafNode("p", "Child text")], props={"class": "container"})
        expected_html = '<div class="container"><p>Child text</p></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_nested_parentnode(self):
        # Test that a nested ParentNode generates the correct HTML
        child = ParentNode("ul", [LeafNode("li", "Item 1"), LeafNode("li", "Item 2")])
        parent = ParentNode("div", [child])
        expected_html = "<div><ul><li>Item 1</li><li>Item 2</li></ul></div>"
        self.assertEqual(parent.to_html(), expected_html)

    def test_multiple_children(self):
        # Test that a ParentNode with multiple children generates the correct HTML
        parent = ParentNode("div", [LeafNode("p", "Paragraph 1"), LeafNode("p", "Paragraph 2")])
        expected_html = "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>"
        self.assertEqual(parent.to_html(), expected_html)

    def test_mixed_parent_and_leaf_nodes(self):
        # Test that a ParentNode with mixed ParentNode and LeafNode children generates the correct HTML
        child = ParentNode("ul", [LeafNode("li", "Item 1"), LeafNode("li", "Item 2")])
        parent = ParentNode("div", [LeafNode("p", "Paragraph"), child])
        expected_html = "<div><p>Paragraph</p><ul><li>Item 1</li><li>Item 2</li></ul></div>"
        self.assertEqual(parent.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()