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

def split_nodes_delimiter(nodes, delimiter):
    result = []
    current_group = []
    
    for node in nodes:
        if node.text == delimiter:
            if current_group:
                result.append(current_group)
                current_group = []
        else:
            current_group.append(node)
    
    if current_group:
        result.append(current_group)
    
    return result   

def extract_markdown_text(nodes):
    texts = []
    for node in nodes:
        if isinstance(node, HtmlNode):
            texts.append(node.text)
            texts.extend(extract_markdown_text(node.children))
    return texts

def split_nodes_by_image(old_nodes):
    result = []
    current_group = []
    
    for node in old_nodes:
        if node.tag == 'img':
            if current_group:
                result.append(current_group)
                current_group = []
            result.append([node])
        else:
            current_group.append(node)
    
    if current_group:
        result.append(current_group)
    
    return result   

def split_nodes_link(old_nodes):
    result = []
    current_group = []
    
    for node in old_nodes:
        if node.tag == 'a':
            if current_group:
                result.append(current_group)
                current_group = []
            result.append([node])
        else:
            current_group.append(node)
    
    if current_group:
        result.append(current_group)
    
    return result

def text_to_textnodes(text):
    return [HtmlNode('span', text=part) for part in text.split()]

def markdown_to_blocks(markdown):
    lines = markdown.split('\n')
    blocks = []
    current_block = []
    
    for line in lines:
        if line.strip() == '':
            if current_block:
                blocks.append(current_block)
                current_block = []
        else:
            current_block.append(HtmlNode('p', text=line))
    
    if current_block:
        blocks.append(current_block)
    
    return blocks

class BlockType(Enum):
    PARAGRAPH = "Paragraph"
    HEADING = "Heading"
    CODE = "Code"
    QUOTE = "Quote"
    UNDERORDERED_LIST = "Unordered List"
    ORDERED_LIST = "Ordered List"

def block_to_blocktype(block):
    if block.tag == 'p':
        return BlockType.PARAGRAPH
    elif block.tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        return BlockType.HEADING
    elif block.tag == 'code':
        return BlockType.CODE
    elif block.tag == 'blockquote':
        return BlockType.QUOTE
    elif block.tag == 'ul':
        return BlockType.UNDERORDERED_LIST
    elif block.tag == 'ol':
        return BlockType.ORDERED_LIST
    else:
        return None

def markdown_to_html_nodes(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        for node in block:
            html_nodes.append(node)
    return html_nodes