from htmlnode import HTMLNode
from block import BlockType,block_to_block_type
from delimiters import text_to_textnodes
from textnode import text_node_to_html_node,TextNode,TextType
from htmlnode import ParentNode
def markdown_to_blocks(markdown):
    blck = []
    raw_blocks = markdown.split("\n\n")
    for block in raw_blocks:
        cleaned = "\n".join(line.strip() for line in block.splitlines()).strip()
        if cleaned:
            blck.append(cleaned)
    return blck
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p",children)
def heading_to_html(block):
    level = 0
    for char in block:
        if char == "#":
            level+=1
        else:
            break
    if level +1>= len(block):
        raise ValueError(f"invalid markdown ##")
    text = block[level+1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}",children)
def code_to_html_node(block):
    if not block.startswith("```"):
        raise ValueError("invalid code")
    splits = block.split("```")
    text = block[4:-3]
    raw_text_node = TextNode(text,TextType.TEXT)
    node = text_node_to_html_node(raw_text_node)
    code = ParentNode("code",[node])
    return ParentNode("pre",[code])
def ordered_list_to_html_node(block):
    lines = block.split("\n")
    html_item = []
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        html_item.append(ParentNode("li",children))
    return ParentNode("ol",html_item)
def unordered_list_to_html_node(block):
    lines = block.split("\n")
    html_item = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_item.append(ParentNode("li",children))
    return ParentNode("ul",html_item)
def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid markdown Quote")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote",children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.HEADING:
        return heading_to_html(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html(block) 
    raise ValueError("Invalid block type") 
    
def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    children = []
    for block in markdown_blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div",children)

# def extract_title(markdown):
    