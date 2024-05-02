from elem import Elem, Text
from elements import *
from colorama import Fore
class Page():
    def __init__(self, root: Elem) -> None:
        self.root = root
    
    def _validate_html(self, node):
        if len(node.content) != 2:
            raise ValueError("Html node must contain 2 elements.")

        if not isinstance(node.content[0], Head):
            raise TypeError("The first child of Html node must be a Head.")
        
        if not isinstance(node.content[1], Body):
            raise TypeError("The second child of Html node must be a Body")

        return True

    def _validate_head(self, node):
        if not node.content:
            raise ValueError("Head cannot be empty")
        
        if len(node.content) != 1:
            raise ValueError("Head must only contain one element.")
        
        if not isinstance(node.content[0], Title):
            raise TypeError("Head must only contain one Title")
        
        return True


    def _validate_body(self, node):
        allowed_elements = [H1, H2, Div, Table, Ul, Ol, Span, Text]
        
        for child in node.content:
            if type(child) not in allowed_elements:
                raise TypeError('Body must only contain the following types of elements: H1, H2, Div, Table, Ul, Ol, Span, Text')

        return True

    def _validate_div(self, node):
        allowed_elements = [H1, H2, Div, Table, Ul, Ol, Span, Text]
        
        for child in node.content:
            if type(child) not in allowed_elements:
                raise TypeError('Div must only contain the following types of elements: H1, H2, Div, Table, Ul, Ol, Span, Text')
        return True

    def _validate_title(self, node):
        if len(node.content) != 1:
            raise ValueError("Title must contain one element")
        if not isinstance(node.content[0], Text):
            raise TypeError("Title must contain only Text")
        return True

    def _validate_H1(self, node):
        if len(node.content) != 1:
            raise ValueError("H1 must contain one element")
        if not isinstance(node.content[0], Text):
            raise TypeError("H1 must contain only Text")
        return True

    def _validate_H2(self, node):
        if len(node.content) != 1:
            raise ValueError("H2 must contain one element")
        if not isinstance(node.content[0], Text):
            raise TypeError("H2 must contain only Text")
        return True

    def _validate_Li(self, node):
        if len(node.content) != 1:
            raise ValueError("H2 must contain one element")
        if not isinstance(node.content[0], Text):
            raise TypeError("H2 must contain only Text")
        return True             

    def is_valid(self):

        validation_dict = {
            Html: self._validate_html,
            Head: self._validate_head,
            Body: self._validate_body,
            Title: self._validate_title,
            H1: self._validate_h1,
            H2: self._validate_h2,
            Li: self._validate_Li,
            Th: self._validate_Th,
            Td: self._validate_Td,
            
        }

        def validate(node):

            validate_func = validation_dict.get(type(node), False)
            
            # check if node type is in validation dict
            if not validate_func:
                # print(Fore.RED, f'invalid type', Fore.RESET)
                return False

            # attempt to validate node 
            try:
                validate_func(node)
            except Exception as e:
                print(e)
                return False

            # recursively check each node
            if hasattr(node, 'content'):
                for child in node.content:
                    # print(Fore.YELLOW, 'child', child, Fore.RESET)
                    if not validate(child):
                        # print(Fore.RED, 'INVALID', Fore.RESET)
                        return False

            return True
        
        # print(Fore.GREEN, "valid node", Fore.RESET)

        return validate(self.root)

if __name__ == "__main__":
    test_2 = Html([
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

    test = Page(test_2).is_valid()
