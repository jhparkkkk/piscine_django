import unittest
from unittest.mock import patch, mock_open
from render import parse_argument, read_template, render_template, escape_html, save_file

class TestRender(unittest.TestCase):
    def test_parse_argument(self):
        """Test parse_argument()
        """
        valid_args = ['render.py', 'filename.template']
        with patch('sys.argv', valid_args):
            self.assertEqual(parse_argument(), 'filename.template')

        invalid_number_args = ['render.py', 'filename.template', 'one.more.arg']
        with patch('sys.argv', invalid_number_args):
            with self.assertRaises(AssertionError) as cm:
                parse_argument()
            self.assertEqual(str(cm.exception), "Usage: python3 render.py 'filename.template'")

        invalid_args = ['render.py', 'filename.jpeg']
        with patch('sys.argv', invalid_args):
            with self.assertRaises(ValueError):
                parse_argument()

    def test_escape_html(self):
        """Test escape_html()
        """
        self.assertEqual(escape_html('Ben & Jerry\'s'), 'Ben &amp; Jerry&#39;s')
        self.assertEqual(escape_html('<script>"XSS" Attack<\script>'), '&lt;script&gt;&quot;XSS&quot; Attack&lt;\script&gt;')
        self.assertEqual(escape_html(''), '')
        with self.assertRaises(TypeError):
            escape_html({1:2, 3:4})
    
    def test_read_template(self):
        """Test read_template()
        """
        mocked_file_content = "Hello {name}!"
        with patch('builtins.open', mock_open(read_data=mocked_file_content)):
            self.assertEqual(read_template('example.template'), "Hello {name}!")

        with patch('builtins.open', side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                read_template('nonexistent_file.template')
        
    def test_render_template(self):
        """ Test if the template renders correctly with provided data. """
        template = "Hello, {name}!"
        result = render_template(template)
        self.assertEqual(result, "Hello Jee!")  

if __name__ == '__main__':
    unittest.main()