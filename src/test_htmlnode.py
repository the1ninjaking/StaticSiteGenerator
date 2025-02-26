import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_html_data(self):
        node = HTMLNode("a", "link", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "link")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"href": "https://www.google.com", "target": "_blank"})
    
    def test_html_default_data(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_html_props_to_html(self):
        node = HTMLNode("a", "link", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "link", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">link</a>')

    def test_invalid_value(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()