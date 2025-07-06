from src.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if tag is None:
            raise ValueError("Parent node need tag")
        if children is None:
            raise ValueError("Parent node need children")
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node need tag")
        if self.children is None:
            raise ValueError("Parent node need children")
        
        return f"<{self.tag}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"