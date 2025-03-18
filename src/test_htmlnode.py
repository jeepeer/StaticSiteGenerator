import unittest

from htmlnode import HtmlNode


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

    def test_props_to_html03(self):
        props = {
            "href": "https://www.google.com",
            "target": "not_blank"
        }
        node = HtmlNode(None, None,None, props)
        self.assertEqual(
            f" href=\"https://www.google.com\" target=\"not_blank\"", node.props_to_html()
        )

if __name__ == "__main__":
    unittest.main() 