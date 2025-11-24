from enum import Enum
# In textnode.py create an enum called TextType. It should cover all the types of text nodes mentioned above.
# In textnode.py create a class called TextNode. It should have 3 properties that can be set in the constructor:
# self.text - The text content of the node
# self.text_type - The type of text this node contains, which is a member of the TextType enum.
# self.url - The URL of the link or image, if the text is a link. Default to None if nothing is passed in.
# Create an __eq__ method that returns True if all of the properties of two TextNode objects are equal. Our future unit tests will rely on this method to compare objects.
# Create a __repr__ method that returns a string representation of the TextNode object. It should look like this:
# TextNode(TEXT, TEXT_TYPE, URL)
# Where TEXT, TEXT_TYPE, and URL are the values of the text, text_type, and url properties, respectively.
# You can get the string representation of the text_type enum by using the .value field.\
#Create a main() function in main.py and call it. The function should create a new TextNode object with some dummy values. Print the object, and make sure it looks like you'd expect. For example, my code printed:
class TextType(Enum):
    PLAIN_TEXT = "Plain Text"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Code"
    ANCHOR = "Anchor"
    IMAGE = "Image"
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'
    def render(self):
        if self.text_type == TextType.PLAIN_TEXT:
            return self.text
        elif self.text_type == TextType.BOLD:
            return f"<strong>{self.text}</strong>"
        elif self.text_type == TextType.ITALIC:
            return f"<em>{self.text}</em>"
        elif self.text_type == TextType.CODE:
            return f"<code>{self.text}</code>"
        elif self.text_type == TextType.ANCHOR:
            return f'<a href="{self.url}">{self.text}</a>'
        elif self.text_type == TextType.IMAGE:
            return f'<img src="{self.url}" alt="{self.text}"/>'
        else:
            return self.text
# TextNode(Hello, World!, Plain Text, None)

