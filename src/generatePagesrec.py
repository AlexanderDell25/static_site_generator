import os
from blockmarkdown import *
from htmlnode import *
from extracttitle import *


def generate_pages_recursive(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    for item in os.listdir(from_path):
        item_path = os.path.join(from_path, item)
        destination_path = os.path.join(dest_path, item)
        if os.path.isfile(item_path) and item_path.endswith(".md"):
            
            # Open and read the content of the source file
            with open (item_path, "r") as file:
                content = file.read()
            #print(f"{item_path} copied to {destination_path}")
            
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

            html_destination = destination_path.replace(".md", ".html")

            # Write the new content to the destination file
            if not os.path.exists(os.path.dirname(html_destination)):
                os.makedirs(os.path.dirname(html_destination))
            with open(html_destination, "w") as file:
                
                file.write(template)
            print(f"Page generated at {html_destination}") 
        elif os.path.isdir(item_path):
            os.makedirs(destination_path, exist_ok=True)  # Ensure the subdirectory exists
            #print(f"new folder created at {destination_path}")
            generate_pages_recursive(item_path, template_path, destination_path) # Recursively generate subfolders
        else:
            print(f"{item_path} is not a markdown file.")
            continue
    
    

    
