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
        elif self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"