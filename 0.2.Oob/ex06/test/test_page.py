import unittest
from elem import Elem
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br
from Page import Page

class TestPage(unittest.TestCase):
    def test_invalid_node(self):
        """Test invalid node
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
        self.assertEqual(Page(Html([Head(), InvalidNodeHtml()])).is_valid(), False)
    
    def test_valid_node(self):
        self.assertEqual(Page(Html()).is_valid(), True)

    
                                                                                                                                                                                                                                                                                                                                   

if __name__ == "__main__":
    unittest.main()