from textnode import TextNode

def main():
    TestText = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(TestText.__repr__)

main()