from src.htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag=None, value=None, children=None, props=None):
        if children is not None:
            raise ValueError("LeafNode can not have children!")
        if value is None:
            raise ValueError("LeafNode must have value!")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}>{self.value}</{self.tag}>"