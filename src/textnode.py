from enum import Enum, auto

class TextType(Enum):
    BOLD = 1
    ITALIC = 2
    UNDERLINE = 3
    STRIKETHROUGH = 4
    CODE = 5
    LINK = 6
    IMAGE = 7
    HEADING = 8
    PARAGRAPH = 9
    TEXT = 10
    # ...add other text types as needed...

class TextNode:
    def __init__(self, text, text_type, url=""):
        self.text = text
        self.text_type = text_type
        self.url = url if url else None
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.name}, {self.url})"