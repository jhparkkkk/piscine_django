import unittest
from elem import Elem
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br
from elements import Text
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

        cases = [
            InvalidNodeElem(),
            Html(InvalidNodeElem()),
            InvalidNodeHtml(),
            Html([Head(Title()), InvalidNodeHtml()])
        ]
        
        for case in cases:
            with self.subTest(case=case):
                page = Page(case)
                self.assertFalse(page.is_valid())


class TestHtml(unittest.TestCase):
    """
    Tests for validating the structure of Html element.
    """
    def test_valid_html(self):
        """test valid html element
        """
        valid_html = Page(Html([Head(), Body()]))
        self.assertTrue(valid_html._validate_html(valid_html.root))

    def test_html_invalid_child_count(self):
        """test html element with wrong numbers of child nodes
        """
        cases = [
            (Html(), "empty Html"),
            (Html([Head()]), "Html with only one element"),
            (Html([Head(), Head(), Head()]), "Html with more than two elements")
        ]

        for case, description in cases:
            with self.subTest(description=description):
                page = Page(case)
                self.assertFalse(page.is_valid())
                with self.assertRaises(ValueError, msg=f"HTML with {description} did not raise ValueError"):
                    page._validate_html(page.root)
                
    
    def test_html_without_mandatory_head(self):
        """test html element without Head as first child node 
        """
        page = Page(Html([Body(), Head()]))

        self.assertFalse(page.is_valid())

        with self.assertRaises(TypeError):
            page._validate_html(page.root)

    def test_html_without_mandatory_Body(self):
        """test html element without Body as second child node 
        """

        page = Page(Html([Head(), Head()]))
        
        self.assertFalse(page.is_valid())
        
        with self.assertRaises(TypeError):
            page._validate_html(page.root)

class TestHead(unittest.TestCase):
    allowed_elements = [Title]
    min_nb = None
    max_nb = 1
    def test_valid_head(self):
        """test valid head element
        """
        valid_head = Head(Title())
        page = Page(valid_head)
        self.assertTrue(page._validate_node(page.root, self.allowed_elements, self.min_nb, self.max_nb))

    def test_empty_head(self):
        """test empty head
        """
        page = Page(Head())
        with self.assertRaises(ValueError):
            page._validate_node(page.root, self.allowed_elements, self.min_nb, self.max_nb)
    
    def test_head_invalid_child_count(self):
        """test head with invalid number of child nodes
        """
        page = Page(Head([Body(), Body()]))
        with self.assertRaises(ValueError):
            page._validate_node(page.root, self.allowed_elements, self.min_nb, self.max_nb)


    def test_head_without_mandatory_title(self):
        """test head without its mandatory Title
        """
        page = Page(Head(Body()))
        with self.assertRaises(TypeError):
            page._validate_node(page.root, self.allowed_elements, self.min_nb, self.max_nb)

class TestBody(unittest.TestCase):
    allowed_elements = [H1, H2, Div, Table, Ul, Ol, Span, Text]
    min_nb = None
    max_nb = None
    def test_valid_body(self):
        """test valid body element
        """
        cases = [
            Body(),
            Body(Text()),
            Body([H1(), H2(), Div(), Table(), Ul(), Ol(), Span(), Text()])
            
        ]
        for case in cases:
            page = Page(case)
            self.assertTrue(page._validate_node(page.root, self.allowed_elements, self.min_nb, self.max_nb))


    def test_body_invalid_child_nodes(self):
        """test body with invalid child nodes
        """
        cases = [
            Body(Body()),
            Body([Html(), Text("Plop")]),
            Body(Title())
        ]

        for case in cases:
            page = Page(case)
            with self.assertRaises(TypeError):
                page._validate_node(page.root, self.allowed_elements, self.min_nb, self.max_nb)

class TestDiv(unittest.TestCase):
    allowed_elements = [H1, H2, Div, Table, Ul, Ol, Span, Text]
    min_nb = None
    max_nb = None
    def test_valid_div(self):
        """test valid body element
        """
        cases = [
            Div(),
            Div(Text()),
            Div([H1(), H2(), Div(), Table(), Ul(), Ol(), Span(), Text()])
            
        ]
        for case in cases:
            page = Page(case)
            self.assertTrue(page._validate_node(page.root, self.allowed_elements, self.min_nb, self.max_nb))

    def test_div_invalid_child_nodes(self):
        """test body with invalid child nodes
        """
        cases = [
            Div(Body()),
            Div([Html(), Text("Plop")]),
            Div(Title())
        ]

        for case in cases:
            page = Page(case)
            with self.assertRaises(TypeError):
                page._validate_node(page.root, self.allowed_elements, self.min_nb, self.max_nb)

class TestTitle(unittest.TestCase):
    allowed_elements = [Text]
    min_nb = None
    max_nb = 1
    def test_valid_title(self):
        """test valid title
        """
        valid_title = Title(Text("This is title"))
        page = Page(valid_title)
        self.assertTrue(page._validate_node(page.root, self.allowed_elements, self.min_nb, self.max_nb))           

class TestTr(unittest.TestCase):
    allowed_elements = [Th, Td]
    min_nb = 1
    max_nb = None

    def test_valid_tr(self):
        """test valid tr
        """
        cases = [
            Tr(Th()),
            Tr(Td()),
            Tr([Th(), Th(), Th()]),
            Tr([Td(), Td(), Td()]),
        ]

        for case in cases:
            page = Page(case)
            self.assertTrue(page._validate_node(page.root, self.allowed_elements, self.min_nb, self.max_nb))           

    def test_mixed_tr(self):
        cases = [
            Tr(Tr()),
            Tr([Div(), Div(), Div()]),
            Tr([Th(), Td()]),
            Tr([Th(), Th(),Text()])
        ]

        for case in cases:
            page = Page(case)
            with self.assertRaises(TypeError):
                page._validate_node(page.root, self.allowed_elements, self.min_nb, self.max_nb)


class TestTable(unittest.TestCase):
    allowed_elements = [Tr]
    min_nb = None
    max_nb = None

    def test_valid_table(self):
        cases = [
            Table(),
            Table(Tr()),
            Table([Tr(), Tr(), Tr()])
        ]

        for case in cases: 
            page = Page(case)
            self.assertTrue(page._validate_node(page.root, self.allowed_elements, self.min_nb, self.max_nb))           

    def test_table_invalid_child_nodes(self):
        cases = [
            Table(H1()),
            Table([H1(), Tr()]),
            Table([Tr(), H1()]),
        ]
        for case in cases:
            page = Page(case)
            with self.assertRaises(TypeError):
                page._validate_node(page.root, self.allowed_elements, self.min_nb, self.max_nb)

if __name__ == "__main__":
    unittest.main()