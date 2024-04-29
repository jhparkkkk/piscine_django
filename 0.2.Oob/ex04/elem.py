class Text(str):
    def __str__(self):
        escaped_text = (super().__str__()
                        .replace('<', '&lt;')
                        .replace('>', '&gt;')
                        .replace('"', '&quot;'))
        return escaped_text.replace('\n', '\n<br />\n')

class Elem:
    class ValidationError(Exception):
        """Exception raised for errors in the input."""
        pass

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag
        self.attr = dict(attr)
        self.tag_type = tag_type
        self.set_content(content)

    
    def set_content(self, content):
        if content is None:
            self.content = []
        elif isinstance(content, (Elem, Text, list)):
            self.content = [content] if not isinstance(content, list) else content
            if not all(isinstance(item, (Elem, Text)) for item in self.content):
                raise self.ValidationError("Content must be an Elem, Text, or a list of these.")
        else:
            raise self.ValidationError("Content must be an Elem, Text, or a list of these.")


    def __str__(self):
        attr_str = self.__make_attr()
        content_str = self.__make_content(1)
        if self.tag_type == 'double':
            if content_str.strip(): 
                return f"<{self.tag}{attr_str}>\n{content_str}\n</{self.tag}>"
            else:
                return f"<{self.tag}{attr_str}></{self.tag}>"
        else:
            return f"<{self.tag}{attr_str} />"

    def __make_attr(self):
        return ''.join(f' {attr}="{value}"' for attr, value in self.attr.items())

    def __make_content(self, indent_level):
        if not self.content:
            return ''
        
        indent = '  ' * indent_level
        content_lines = []
        for elem in self.content:
            if isinstance(elem, Elem):
                element_string = elem.__str__()
                indented_element = '\n'.join(indent + line for line in element_string.split('\n'))
                content_lines.append(indented_element)
            elif isinstance(elem, Text) and str(elem).strip():
                content_lines.append(indent + str(elem))

        return '\n'.join(content_lines)

    def add_content(self, new_content):
        if not self.check_type(new_content):
            raise self.ValidationError("incorrect behaviour.")
        if isinstance(new_content, list):
            self.content.extend(new_content)
        else:
            self.content.append(new_content)

    @staticmethod
    def check_type(content):
        return isinstance(content, (Elem, Text)) or \
               (isinstance(content, list) and all(isinstance(elem, (Elem, Text)) for elem in content))

if __name__ == "__main__":
    title = Elem(tag='title', content=Text("Hello ground!"), tag_type='double')
    head = Elem(tag='head', content=title, tag_type='double')
    
    h1 = Elem(tag='h1', content=Text("Oh no, not again!"), tag_type='double')
    img = Elem(tag='img', attr={'src': "http://i.imgur.com/pfp3T.jpg"}, tag_type='simple')
    
    body = Elem(tag='body', content=[h1, img], tag_type='double')
    
    html = Elem(tag='html', content=[head, body], tag_type='double')
    
    print(html)