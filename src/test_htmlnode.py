import unittest

from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_1(self):
        node = HTMLNode(
            tag="Node 1", 
            value="some_value", 
            props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(node.props_to_html(), "href=\"https://www.google.com\" target=\"_blank\"")


if __name__ == "__main__":
    unittest.main()