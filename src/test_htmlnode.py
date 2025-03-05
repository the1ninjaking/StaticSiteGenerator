import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_multi_grandchildren(self):
        grandchild_node1 = LeafNode("a", "grandchild1")
        grandchild_node2 = LeafNode("b", "grandchild2")
        grandchild_node3 = LeafNode("c", "grandchild3")
        child_node1 = ParentNode("e", [grandchild_node1, grandchild_node2])
        child_node2 = ParentNode("f", [grandchild_node3])
        parent_node = ParentNode("g", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<g><e><a>grandchild1</a><b>grandchild2</b></e><f><c>grandchild3</c></f></g>",
        )


if __name__ == "__main__":
    unittest.main()