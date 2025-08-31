import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p","Hello, world!")
        self.assertEqual(node.to_html(),"<p>Hello, world!</p>")
    def test_leaf_to_html_p1(self):
        node = LeafNode("t","Hello, world!")
        self.assertNotEqual(node.to_html(),"<p>Hello, world!</p>")
    def test_leaf_to_html_p2(self):
        node = LeafNode("div","Hello, world!")
        self.assertEqual(node.to_html(),"<div>Hello, world!</div>")
    def test_leaf_to_html_p3(self):
        node = LeafNode("div","Hello,manav!")
        self.assertNotEqual(node.to_html(),"<div>Hello, world!</div>")
if __name__=="__main__":
    unittest.main()
