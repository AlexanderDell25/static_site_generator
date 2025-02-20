from enum import Enum, auto
from textnode import TextNode, TextType
from splitnodesdelimiter import text_to_text_nodes
from htmlnode import *

def markdown_to_blocks(markdown):
    # Split markdown into blocks by double newlines
    blocks = markdown.split("\n\n")
    
    # Strip leading and trailing whitespace from each block
    blocks = [block.strip() for block in blocks]
    
    # Remove empty blocks
    blocks = [block for block in blocks if block]
    
    return blocks

# Example usage
"""
document = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
print(document)
print(markdown_to_blocks(document))  # ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
"""

class BlockType(Enum):
    # Define block types as enum values
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"

def block_to_block_type(block):
    # Split the block into lines
    lines = block.split("\n")

    # Check if the block is a heading
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    # Check if the block is a code block
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    # Check if the block is a quote
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    # Check if the block is an unordered list (starts with "* ")
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    
    # Check if the block is an unordered list (starts with "- ")
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    
    # Check if the block is an ordered list (starts with "1. ", "2. ", etc.)
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    
    # Default to paragraph if no other type matches
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    # Split markdown into blocks
    blocks = markdown_to_blocks(markdown)
    
    # Initialize a list to hold the HTML nodes
    html_nodes = []
    
    # Iterate over each block
    for block in blocks:
        # Determine the block type
        block_type = block_to_block_type(block)
        
        # Create an HTML node based on the block type
        if block_type == BlockType.HEADING:
            # Extract the heading level and text
            level = block.count("#")
            text = block.strip("# ")
            html_nodes.append(LeafNode(f"h{level}", text))
        elif block_type == BlockType.CODE:
            # Extract the code text
            code_lines = block.split("\n")[1:-1]
            code_text = "\n".join(code_lines)
            html_nodes.append(ParentNode("pre", [LeafNode("code", code_text)]))
        elif block_type == BlockType.QUOTE:
            # Extract the quote text
            quote_lines = [line.strip("> ") for line in block.split("\n")]
            quote_text = "\n".join(quote_lines)
            html_nodes.append(ParentNode("blockquote", text_to_children(quote_text)))
        elif block_type == BlockType.ULIST:
            # Extract the list items
            list_items = [line.strip("* ") for line in block.split("\n")]
            list_item_nodes = [LeafNode("li", item) for item in list_items]
            html_nodes.append(ParentNode("ul", list_item_nodes))
        elif block_type == BlockType.OLIST:
            # Extract the list items
            list_items = [line.split(". ")[1] for line in block.split("\n")]
            list_item_nodes = [LeafNode("li", item) for item in list_items]
            html_nodes.append(ParentNode("ol", list_item_nodes))
        else:
            # Default to paragraph
            html_nodes.append(ParentNode("p", text_to_children(block)))
    
    # Create a single parent HTML node (div) containing all the block nodes
    parent_node = ParentNode("div", html_nodes)
    
    return parent_node


def text_to_children(text):
    # Convert text to TextNodes
    text_nodes = text_to_text_nodes(text)
    
    # Convert TextNodes to HTMLNodes
    html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]
    
    return html_nodes
