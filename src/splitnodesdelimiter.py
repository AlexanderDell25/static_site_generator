from htmlnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if isinstance(node, TextNode) and node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    # Even index parts are plain text
                    if part:
                        new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    # Odd index parts are the specified text type
                    if part:
                        new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)
    
    return new_nodes