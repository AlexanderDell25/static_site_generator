from textnode import TextNode, TextType

class HTMLNode(object):
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

        if self.tag  == "":
            self.tag = TextNode("", TextType.NORMAL)

        if self.value == "":
            self.value = children

        if self.children == None:
            self.children = value

        if self.props == None:
            self.tag = ""
            self.value = ""
            self.children = []
            self.props = {}


    def to__html(self):
        raise NotImplementedError
        
    def props_to_html(self):
        href = self.props.lstrip.get('href')
        target = self.props.lstrip.get('target')
        return f"href={href} target={target}"
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"