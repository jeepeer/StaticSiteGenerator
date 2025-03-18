import unittest

from htmlnode import HtmlNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html01(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HtmlNode(None, None,None, props)
        self.assertEqual(
            f" href=\"https://www.google.com\" target=\"_blank\"", node.props_to_html()
        )

    def test_props_to_html02(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            "additional_target": "_blank"
        }
        node = HtmlNode(None, None,None, props)
        self.assertEqual(
            f" href=\"https://www.google.com\" target=\"_blank\" additional_target=\"_blank\"", node.props_to_html()
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )
    
    def test_leaf_to_html_none(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main() 