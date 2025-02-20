from blockmarkdown import *

def extract_title(markdown):
    # Split markdown into blocks
    blocks = markdown_to_blocks(markdown)
    
    # Find the first heading block
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING:
            block = block.strip()
            block = block.replace("# ", "")
            return block
    
    # Raise Exception if there is no heading block
    raise Exception("No heading block found")
