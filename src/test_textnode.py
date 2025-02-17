import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, TextNode("This is a text node", TextType.ITALIC))
        #self.assertEqual(node, TextNode("This is a text node", TextType.BOLD, "https://www.example.com"))
        #self.assertEqual(node, TextNode("This is a text node", TextType.BOLD, ""))
    
    def test_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, TextNode("This is a text node", TextType.ITALIC, ""))
        self.assertNotEqual(node, TextNode("This is a text node", TextType.BOLD, "https://www.example.com"))
        self.assertNotEqual(node, TextNode("This is a text node", TextType.BOLD, "https://www.example.com"))

if __name__ == "__main__":
    unittest.main()