# linked to ./main.sh in root directory
import os
from htmlnode import *
from textnode import *
from copystatic import *
from generatePagesrec import *

def main():
    #text_node = TextNode("Hello, World!", TextType.H1, "https://www.example.com")  # Create a TextNode object
    #print(text_node)  # Output: TextNode(Hello, World!, H1, https://www.example.com)
    
    # Delete everything in source and copy everything from source to destination
    source = "static"
    destination = "public"
    copy_delete_folder(source, destination)

    # Generate the index page
    from_path = "content"
    template_path = "template.html"
    dest_path = "public"

    generate_pages_recursive(from_path, template_path, dest_path)

if __name__ == "__main__":
    main()