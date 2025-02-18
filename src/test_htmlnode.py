import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node, node2)
        
    
    def test_uneq(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode(props={"href": "https://www.google.com", "target": "blank",})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()