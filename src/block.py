from enum import Enum
import re
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING  = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = " unordered_list"
    ORDERED_LIST = "ordered_list"
def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in block.split("\n")):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in block.split("\n")):
        return BlockType.UNORDERED_LIST
    elif all(re.match(r"^\d+\.\s",line) for line in block.split("\n")):
        lines=block.split("\n")
        for i, line in enumerate(lines, start=1):
            num = int(re.match(r"^(\d+)\.\s", line).group(1))
            if num != i:
                return BlockType.PARAGRAPH  # Not valid ordered list
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH