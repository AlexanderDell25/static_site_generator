import re

def extract_markdown_images(text):
    image_nodes = []  # Initialize an empty list to store the image nodes
    image_pattern = r"!\[([^\]]*)\]\(([^)]*)\)"  # Define the regex pattern to match markdown image syntax
    matches = re.finditer(image_pattern, text)  # Find all matches of the pattern in the input text
    
    for match in matches:
        alt_text = match.group(1)  # Extract the alt text from the match
        url = match.group(2)  # Extract the URL from the match
        alt_url = (alt_text, url) # Create a tuple with alt text and url 
        image_nodes.append(alt_url) # Append the tuple to the list of image nodes
    return image_nodes  # Return the list of image nodes

def extract_markdown_links(text):
    link_nodes = []  # Initialize an empty list to store the image nodes
    image_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"  # Define the regex pattern to match markdown image syntax
    matches = re.finditer(image_pattern, text)  # Find all matches of the pattern in the input text
    
    for match in matches:
        text = match.group(1)  # Extract the text from the match
        url = match.group(2)  # Extract the URL from the match
        text_url = (text, url) # Create a tuple with text and url 
        link_nodes.append(text_url) # Append the tuple to the list of image nodes
    return link_nodes  # Return the list of image nodes

#print(extract_markdown_images("![Image alt text](https://www.example.com/image.png) and ![Image alt text2](https://www.example2.com/image.png)"))  # Test the function with a sample input
#print(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"))  # Test the function with a sample input