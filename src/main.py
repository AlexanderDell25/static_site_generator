# linked to ./main.sh in root directory
from textnode import TextNode, TextType

def main():
    text_node = TextNode("Hello, World!", TextType.H1, "https://www.example.com")  # Create a TextNode object
    print(text_node)  # Output: TextNode(Hello, World!, H1, https://www.example.com)

main()