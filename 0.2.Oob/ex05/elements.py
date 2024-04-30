from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('html', attr, content)

class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('head', attr, content)

class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('body', attr, content)

class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('title', attr, content)

class Meta(Elem):
    def __init__(self, attr={}):
        super().__init__('meta', attr, tag_type='simple')

class Img(Elem):
    def __init__(self, attr={}):
        super().__init__('img', attr, tag_type='simple')

class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('table', attr, content)

class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('th', attr, content)

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('tr', attr, content)

class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('td', attr, content)

class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('ul', attr, content)

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('ol', attr, content)

class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('li', attr, content)

class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('h1', attr, content)

class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('h2', attr, content)

class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('p', attr, content)

class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('div', attr, content)

class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('span', attr, content)

class Hr(Elem):
    def __init__(self, attr={}):
        super().__init__('hr', attr, tag_type='simple')

class Br(Elem):
    def __init__(self, attr={}):
        super().__init__('br', attr, tag_type='simple')



if __name__ == "__main__":
    test_1 = Html([
        Head([
            Title(Text("Hello Ground!"))
        ]),
        Body([
            H1(Text("Oh no, not again!")),
            Img({"src":"http://i.imgur.com/pfp3T.jpg"})
        ])
    ])
    
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

    print(test_1)
    print(test_2)
    with open('test_1.html', "w") as file:
        file.write(str(test_1))
    with open('test_2.html', "w") as file:
        file.write(str(test_2))