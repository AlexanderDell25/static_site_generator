from htmlnode import TextNode, TextType
from extractmarkdown import extract_markdown_links, extract_markdown_images

def split_nodes_image(old_nodes):
    new_nodes = []  # Initialize an empty list to store the new nodes
    for node in old_nodes:
        if isinstance(node, TextNode) and node.text_type == TextType.TEXT:
            images = extract_markdown_images(node.text)  # Extract images from the text
            if not images:
                new_nodes.append(node)  # If no images, append the original node
                continue

            remaining_text = node.text  # Initialize remaining_text with the full text
            for alt_text, url in images:
                parts = remaining_text.split(f"![{alt_text}]({url})", 1)  # Split the text at the first occurrence of the image
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))  # Append the text before the image as a TextNode
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))  # Append the image as a TextNode with TextType.IMAGE
                remaining_text = parts[1]  # Update remaining_text with the text after the image
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))  # Append any remaining text as a TextNode
        else:
            new_nodes.append(node)  # If the node is not a TextNode or not of type TEXT, append it as is
    return new_nodes  # Return the list of new nodes

def split_nodes_link(old_nodes):
    new_nodes = []  # Initialize an empty list to store the new nodes
    for node in old_nodes:
        if isinstance(node, TextNode) and node.text_type == TextType.TEXT:
            links = extract_markdown_links(node.text)  # Extract links from the text
            if not links:
                new_nodes.append(node)  # If no links, append the original node
                continue

            remaining_text = node.text  # Initialize remaining_text with the full text
            for text, url in links:
                parts = remaining_text.split(f"[{text}]({url})", 1)  # Split the text at the first occurrence of the link
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))  # Append the text before the link as a TextNode
                new_nodes.append(TextNode(text, TextType.LINK, url))  # Append the link as a TextNode with TextType.LINK
                remaining_text = parts[1]  # Update remaining_text with the text after the link
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))  # Append any remaining text as a TextNode
        else:
            new_nodes.append(node)  # If the node is not a TextNode or not of type TEXT, append it as is
    return new_nodes  # Return the list of new nodes