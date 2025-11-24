class HtmlNode:
    def __init__(self, tag, attributes=None, children=None, text=''):
        self.tag = tag
        self.attributes = attributes if attributes is not None else {}
        self.children = children if children is not None else []
        self.text = text

    def add_child(self, child_node):
        self.children.append(child_node)

    def set_attribute(self, key, value):
        self.attributes[key] = value

    def render(self):
        attr_str = ' '.join(f'{key}="{value}"' for key, value in self.attributes.items())
        opening_tag = f'<{self.tag} {attr_str}>' if attr_str else f'<{self.tag}>'
        closing_tag = f'</{self.tag}>'
        
        children_str = ''.join(child.render() for child in self.children)
        
        return f'{opening_tag}{self.text}{children_str}{closing_tag}'