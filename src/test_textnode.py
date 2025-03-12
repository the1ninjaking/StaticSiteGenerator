import unittest

from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_diff_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node.text, node2.text)

    def test_diff_texttype(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node.text_type, node2.text_type)

    def test_None(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)
    
    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "webpage")
        self.assertNotEqual(node.url, None)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_image(self):
        node = TextNode("This is a image node", TextType.IMAGE, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["alt"], "This is a image node")
        self.assertEqual(html_node.props["src"], "www.google.com")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "imagelink")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props["href"], "imagelink")

    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)])

    def test_split_nodes_edge(self):
        node = TextNode("**Bold text** starts off this text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("", TextType.TEXT), TextNode("Bold text", TextType.BOLD), TextNode(" starts off this text", TextType.TEXT)])
    
    def test_split_nodes_no_split(self):
        node = TextNode("This is text with nothing else", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with nothing else", TextType.TEXT)])
    
    def test_alot_of_split_nodes(self):
        node1 = TextNode("This is text with nothing else", TextType.TEXT)
        node2 = TextNode("This is italic text already", TextType.ITALIC)
        node3 = TextNode("This is text with a _italic_ word", TextType.TEXT)
        node4 = TextNode("This is text with another _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2, node3, node4], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is text with nothing else", TextType.TEXT), TextNode("This is italic text already", TextType.ITALIC), TextNode("This is text with a ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT), TextNode("This is text with another ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT)])



if __name__ == "__main__":
    unittest.main()