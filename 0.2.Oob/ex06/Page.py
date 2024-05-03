from elem import Elem, Text
from elements import *
from colorama import Fore
class Page():
    def __init__(self, root: Elem) -> None:
        """
        Init with the root element of the page

        Args:
            root (Elem): root element of the page
        """
        self.root = root

    def __str__(self):
        """Generate HTML string with doctype if the root is Html."""
        html_string = str(self.root)
        if isinstance(self.root, Html):
            return f"<!DOCTYPE html>\n{html_string}"
        return html_string

    def write_to_file(self, filename):
        """Write the HTML code to a file, prefixed with doctype if the root is Html."""
        with open(filename, 'w') as file:
            file.write(str(self))
    
    def _validate_html(self, node: Html):
        """
        Validate html structure

        Args:
            node (Html): html node

        Raises:
            ValueError: if Html does not contain exactly 2 elements
            TypeError: if the first child of Html node is not a Head
            TypeError: if the second child of Html node is not a Body

        Returns:
            Bool : true if Html node is valid
        """
        if len(node.content) != 2:
            raise ValueError("Html node must contain 2 elements.")

        if not isinstance(node.content[0], Head):
            raise TypeError("The first child of Html node must be a Head.")
        
        if not isinstance(node.content[1], Body):
            raise TypeError("The second child of Html node must be a Body")

        return True

    def _validate_tr(self, node: Tr):
        """
        Validate Tr structure

        Args:
            node (Tr): Tr node

        Raises:
            TypeError: if Th and Td are mixed in a single Tr

        Returns:
            Bool: True if the Tr node is valid
        """
        if not all(isinstance(child, type(node.content[0])) for child in node.content):
            raise TypeError("TH and TD elements must not be mixed in a single TR")
        
        return True

    def _validate_node(self, node: Elem, allowed_elements: list, min: int, max: int):
        """
        Validate node based on allowed child types and counts

        Args:
            node (Elem): node to examine
            allowed_elements (list): allowed child types the node can have
            min (int): allowed minimum count of child nodes
            max (int): allowes maximum count of child nodes

        Raises:
            ValueError: If node does not contain one element
            ValueError: If node does not contain at least one element
            TypeError: If child node is not allowed for this node 

        Returns:
            _type_: _description_
        """
        if max == 1 and len(node.content) != 1:
            raise ValueError(f"{type(node)} must contain one element")
        
        if min == 1 and len(node.content) < 1:
            raise ValueError(f"{type(node)} must contain at least one element")
            
        for child in node.content:
            if type(child) not in allowed_elements:
                raise TypeError(f'{type(child)} is not allowed for f{type(node)}')

        if type(node) == Tr:
            self._validate_tr(node)

        print(Fore.GREEN, f"Node <{type(node).__name__}> is valid", Fore.RESET)
        return True


    def is_valid(self):
        """
        Validate recursively the entire html structure starting from the root

        Returns:
            Bool : True if the structure is valid
        """

        validation_dict = {
            Html: self._validate_html,
            Head: lambda  x: self._validate_node(x, [Title], None, 1),
            Body: lambda  x: self._validate_node(x, [H1, H2, Div, Table, Ul, Ol, Span, Text], None, None),
            Div: lambda  x: self._validate_node(x, [H1, H2, Div, Table, Ul, Ol, Span, Text], None, None),
            Title: lambda  x: self._validate_node(x, [Text], None, 1),
            H1: lambda  x: self._validate_node(x, [Text], None, 1),
            H2: lambda  x: self._validate_node(x, [Text], None, 1),
            Li: lambda  x: self._validate_node(x, [Text], None, 1),
            Th: lambda  x: self._validate_node(x, [Text], None, 1),
            Td: lambda  x: self._validate_node(x, [Text], None, 1),
            P: lambda  x: self._validate_node(x, [Text], None, None),
            Span: lambda  x: self._validate_node(x, [Text, P], None, None),
            Ul: lambda  x: self._validate_node(x, [Li], 1, None),
            Ol: lambda  x: self._validate_node(x, [Li], 1, None),
            Tr: lambda  x: self._validate_node(x, [Th, Td], 1, None),
            Table: lambda  x: self._validate_node(x, [Tr], None, None),
            Text: lambda x: True
        }

        def validate(node):

            validate_func = validation_dict.get(type(node), False)
            
            # check if node type is in validation dict
            if not validate_func:
                print(Fore.RED, f'invalid type {type(node)}', Fore.RESET)
                return False

            # attempt to validate node 
            try:
                validate_func(node)
            except Exception as e:
                print(Fore.MAGENTA, e, Fore.RESET)
                return False

            # recursively check each node
            if hasattr(node, 'content'):
                for child in node.content:
                    if not validate(child):
                        return False

            return True
        

        return validate(self.root)

if __name__ == "__main__":
    test = Html([
        Head([
            Title(Text("CV"))
        ]),
        Body([
            H1(Text("Jee Park")),
            Div([H2(Text("Experience")),
            Ol([Li(Text("Artist Agent")), Li(Text("Gallery Assistant"))])], {'class': 'Experience'}),
            Div([H2(Text("Education")),
            Ul([Li(Text('Ecole 42 Paris')), Li(Text('Université Paris I'))])], {'class': 'Education'}),
            
            Div([H2(Text("Languages")),
            Table([Tr([Th(Text("Language")), Th(Text("Level"))]),\
                   Tr([Td(Text("French")), Td(Text("Monther tongue"))]),\
                    Tr([Td(Text("English")), Td(Text("Fluent"))]),\
                        Tr([Td(Text("Korean")), Td(Text("Intermediate"))])])          
        ], {'class': 'Languages'})
    ])
    ], {'lang': 'en'})

    test = Page(test)
    print(f"Is this Html document valid? {test.is_valid()}")
    
    print(test.__str__())
    test.write_to_file('test.html')
