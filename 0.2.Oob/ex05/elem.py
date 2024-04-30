class Text(str):
    def __str__(self):
        escaped_text = (super().__str__()
                        .replace('&', '&amp;')
                        .replace('<', '&lt;')
                        .replace('>', '&gt;')
                        .replace('"', '&quot;')
                        .replace("'", '&#39;')
                        .replace("/", '&#x2F;'))
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
        content_str = self.__make_content(indent_level=1)
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
        indent = '  ' * indent_level

        content_lines = []
        for element in self.content:
            if isinstance(element, Elem):
                # convert type Elem to str to create indentation
                element_string = str(element)
                indented_element = '\n'.join(indent + line for line in element_string.split('\n'))
                content_lines.append(indented_element)
            elif isinstance(element, Text) and str(element):
                content_lines.append(indent + str(element))

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
