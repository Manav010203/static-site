import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode(self):
        node = HTMLNode("p","hello")
        self.assertEqual(node.__repr__(),
                         'HTMLNode(p,hello,None,None)')
    # def test_htmlnode1(self):
    #     node = 'HTMLNode(p,hello,ww.mm.com)'
    #     self.assertEqual(node,
    #                      f"HTMLNode(p,hello,ww.mm.com)")
    # def test_htmlnode2(self):
    #     node = HTMLNode(t,hello)
    #     self.assertNotEqual(node,
    #                      f"HTMLNode(p,hello)")
    #     self.assertEqual(node.tag,'t')
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )
    def test_Val(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual('div',node.tag)
        self.assertEqual('Hello, world!',node.value)
        self.assertEqual(None,node.children)
        self.assertEqual(' class="greeting" href="https://boot.dev"',node.props_to_html())

