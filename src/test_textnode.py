import unittest
from textnode import TextNode,TextType
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("manav",TextType.BOLD_TEXT)
        node2 = TextNode("manav",TextType.BOLD_TEXT)
        self.assertEqual(node,node2)
    def test_eq1(self):
        node = TextNode("maav",TextType.BOLD_TEXT)
        node2 = TextNode("manav",TextType.BOLD_TEXT)
        self.assertNotEqual(node,node2)
    def test_eq2(self):
        node = TextNode("manav",TextType.ITALIC_TEXT)
        node2 = TextNode("manav",TextType.BOLD_TEXT)
        self.assertNotEqual(node,node2)
    def test_eq3(self):
        node = TextNode("manav",TextType.ITALIC_TEXT,"ww.mn.com")
        node2 = TextNode("manav",TextType.ITALIC_TEXT,"ww.mn.com")
        self.assertEqual(node,node2)
if __name__=="__main__":
    unittest.main()
