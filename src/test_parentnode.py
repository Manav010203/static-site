import unittest
from htmlnode import ParentNode,LeafNode

class test_parentchild(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", children=[child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", children=[grandchild_node])
        parent_node = ParentNode("div", children=[child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_grandchildren1(self):
        grandchild_node = LeafNode("b", "manav testing")
        child_node = ParentNode("span", children=[grandchild_node])
        parent_node = ParentNode("div", children=[child_node])
        self.assertNotEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("p", "grandchild")
        child_node = ParentNode("span", children=[grandchild_node])
        parent_node = ParentNode("div", children=[child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><p>grandchild</p></span></div>",
        )
    def test_to_html_with_grandchildren(self):
        great_grand_children = LeafNode("b","manav")
        grandchild_node = ParentNode("p",children=[great_grand_children])
        child_node = ParentNode("span", children=[grandchild_node])
        parent_node = ParentNode("div", children=[child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><p><b>manav</b></p></span></div>",
        )
    def test_to_html_with_grandchildren3(self):
        great_grand_children = LeafNode("b","manav")
        # grandchild_node = ParentNode("p",children=[great_grand_children])
        # child_node = ParentNode("span", children=[grandchild_node])
        parent_node = ParentNode("div", children=[great_grand_children])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>manav</b></div>",
        )

if __name__=="__main__":
    unittest.main()