import unittest

from htmlnode import *

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        
        excepted_result = "<p>This is a paragraph of text.</p>"
        excepted_result2 = '<a href="https://www.google.com">Click me!</a>'
        
        self.assertEqual(node.to_html(), excepted_result)
        self.assertEqual(node2.to_html(), excepted_result2)
    
    def test_uneq(self):
        node = LeafNode("p", "First paragraph.")
        node2 = LeafNode("p", "Second paragraph.")

        # Ensure different nodes do not render the same HTML
        self.assertNotEqual(node.to_html(), node2.to_html())

    def test_value_exception(self):
        node = LeafNode("p", "Non-empty value")
        node.value = None  # Simulate invalid state (bypassing constructor check)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_tag(self):
        node = LeafNode(None, "Raw text")
        self.assertEqual(node.to_html(), "Raw text")

if __name__ == "__main__":
    unittest.main()