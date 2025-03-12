from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, type, url=None):
        self.text = text
        self.text_type = type
        self.url = url
    
    def __eq__(self, obj):
        if self.text == obj.text and self.text_type == obj.text_type and self.url == obj.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("invalid TextType")
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for i in old_nodes:
        if i.text_type == TextType.TEXT:
            current_nodes = []

            if i.text.count(delimiter) % 2 == 1:
                raise SyntaxError("invalid Markdown syntax")
            current_nodes = i.text.split(delimiter)
            
            is_text = True

            for n in current_nodes:
                if is_text == True:
                    new_nodes.append(TextNode(n, TextType.TEXT))
                    is_text = False
                else:
                    new_nodes.append(TextNode(n, text_type))
                    is_text = True
        else:
            new_nodes.append(i)
            
    return new_nodes