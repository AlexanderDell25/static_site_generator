

class HTMLNode(object):
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children else []
        self.props = props if props else {}

    def to_html(self):
        raise NotImplementedError
        
    def props_to_html(self):
        html = "".join(f' {key}="{value}"' for key, value in self.props.items() if value is not None)
        return html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return (self.tag == other.tag and
                    self.value == other.value and
                    self.children == other.children and
                    self.props == other.props)
        return False

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)
        self.children = None
    
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have a value")
        elif self.tag == "img":
                return f"<{self.tag}{self.props_to_html()}/>"
        elif self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        elif self.children == None or self.children == []:
            raise ValueError("ParentNode must have children")
        else:
            children_string = ""
            for child in self.children:
                children_string += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"

def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text, None)
        elif text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text, None)
        elif text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text, None)
        elif text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text, None)
        elif text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        elif text_node.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        else:
            raise Exception("Invalid TextType")         