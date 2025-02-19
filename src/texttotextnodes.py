""" from textnode import TextNode, TextType
from splitnodesdelimiter import split_nodes_delimiter
from splitnodesimagelink import split_nodes_image, split_nodes_link

def text_to_text_nodes(text):
    # Start with a single TextNode containing the entire text
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Split nodes by code blocks
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    # Split nodes by bold text
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    
    # Split nodes by italic text
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    
    # Split nodes by images
    nodes = split_nodes_image(nodes)
    
    # Split nodes by links
    nodes = split_nodes_link(nodes)
    
    return nodes
 """