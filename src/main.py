# Create a main() function in main.py and call it. The function should create a new TextNode object with some dummy values. Print the object, and make sure it looks like you'd expect. For example, my code printed:
from textnode import TextNode, TextType

def main():
    # Create a TextNode instance with some sample text
    text_node = TextNode("Hello, World!", TextType.PLAIN_TEXT)
    
    # Print the TextNode object
    print(text_node)

if __name__ == "__main__":
    main()# TextNode(Hello, World!, Plain Text, None)