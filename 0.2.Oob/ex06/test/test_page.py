import unittest
from elem import Elem
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br
from Page import Page

class TestPage(unittest.TestCase):
    def test_invalid_node(self):
        """test invalid node
        """
        class InvalidNodeElem(Elem):
            def __init__(self, content=None, attr={}):
                super().__init__('invalidnode', attr, content)

        class InvalidNodeHtml(Html):
            def __init__(self, content=None, attr=None):
                super().__init__(content, {'invalid_attr': 'invalid_value'})

        self.assertEqual(Page(InvalidNodeElem()).is_valid(), False)
        self.assertEqual(Page(Html(InvalidNodeElem())).is_valid(), False)
        self.assertEqual(Page(InvalidNodeHtml()).is_valid(), False)
        self.assertEqual(Page(Html([Head(Title()), InvalidNodeHtml()])).is_valid(), False)
    

class TestHtml(unittest.TestCase):
    def test_valid_html(self):
        """test valid html element
        """
        html = Page(Html([Head(), Body()]))
        self.assertEqual(html._validate_html(html.root), True)
        self.assertEqual(html.is_valid(), True)


    def test_html_invalid_child_count(self):
        """test html element with wrong numbers of child nodes
        """
        cases = [
            [],
            [Head()],
            [Head(), Head(), Head()]
        ]

        for childen in cases:
            with self.subTest(childen=childen):
                page = Page(Html(childen))
                with self.assertRaises(ValueError):
                    page._validate_html(page.root)

                                                                                                                                                                                                                                                                                                                                   

if __name__ == "__main__":
    unittest.main()