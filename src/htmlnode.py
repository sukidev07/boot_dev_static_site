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

class LeafNode(HtmlNode):
    def __init__(self, tag, attributes=None, text=''):
        super().__init__(tag, attributes, children=None, text=text)

    def render(self):
        attr_str = ' '.join(f'{key}="{value}"' for key, value in self.attributes.items())
        opening_tag = f'<{self.tag} {attr_str} />' if attr_str else f'<{self.tag} />'
        return f'{opening_tag}{self.text}'

class ParentNode(HtmlNode):
    def __init__(self, tag, attributes=None, children=None):
        super().__init__(tag, attributes, children=children, text='')

def text_node_to_html_node(text_node):
    if text_node.text_type == 'bold':
        return HtmlNode('strong', text=text_node.text)
    elif text_node.text_type == 'italic':
        return HtmlNode('em', text=text_node.text)
    else:
        return HtmlNode('span', text=text_node.text)