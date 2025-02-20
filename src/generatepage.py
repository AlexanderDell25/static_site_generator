import os
from blockmarkdown import *
from htmlnode import *
from extracttitle import *


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Open and read the content of the source file
    with open (from_path, "r") as file:
        content = file.read()
    
    # Open and read the content of the template file
    with open (template_path, "r") as file:
        template = file.read()
    
    # Grab title from the title of the page
    title = extract_title(content)

    # Convert markdown file to html
    content = markdown_to_html_node(content)

    # Convert html node to html
    content = content.to_html()

    # Replace the title and content in the template
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    # Write the new content to the destination file
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as file:
        file.write(template)
    print(f"Page generated at {dest_path}")