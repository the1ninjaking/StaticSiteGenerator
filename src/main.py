from textnode import TextNode, TextType

def main():
    TestText = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(TestText.__repr__())

main()