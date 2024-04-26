import sys
import settings


def parse_argument() -> str:
    """
    Parses and validate the command line argument.
    Checks if:
        - Only one argument is given
        - Filename ends with '.template' extension

    Raises:
        AssertionError: invalid number of arguments
        ValueError: invalid file extension name

    Returns:
        str: filename
    """
    assert len(sys.argv) == 2, "Usage: python3 render.py 'filename.template'"

    filename = sys.argv[1]

    if not filename.endswith(".template"):
        raise ValueError("File must end with 'template'")

    return filename


def escape_html(text: str) -> str:
    """
        Escapes HTML special characters in a string ensuring
    data rendered into an HTML context can't be used to perform XSS attacks
    by injecting malicious HTML or JavaScript code

        Args:
        text (str): text to be escaped

        Returns:
        str: escaped text
    """
    if not isinstance(text, str):
        raise TypeError('Text to be escaped must be a string')

    html_escapes = {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}

    return "".join(html_escapes.get(char, char) for char in text)


def read_template(filename: str) -> str:
    """
    Reads and returns the content of a template

    Args:
        filename (str): template's filename

    Returns:
        str: content of the template
    """
    with open(filename, "r") as file:
        template_content = file.read()
    return template_content


def render_template(template_content):
    """
        Renders the template by replacing the placeholders with sanitized data
    retrieved in settings

        Args:
            template_content (str): template content containing placeholders

        Returns:
            str: rendered html content with placeholders replaced
    """
    sanitized_data = {
        "name": escape_html(settings.NAME),
        "profession": escape_html(settings.PROFESSION),
        "age": escape_html(settings.AGE),
        "location": escape_html(settings.LOCATION),
        "education_1_school": escape_html(settings.EDUCATION[0]["school"]),
        "education_1_year": escape_html(settings.EDUCATION[0]["year"]),
        "education_1_degree": escape_html(settings.EDUCATION[0]["degree"]),
        "education_2_school": escape_html(settings.EDUCATION[1]["school"]),
        "education_2_year": escape_html(settings.EDUCATION[1]["year"]),
        "education_2_degree": escape_html(settings.EDUCATION[1]["degree"]),
        "skill_1": escape_html(settings.TECHNICAL_SKILLS[0]),
        "skill_2": escape_html(settings.TECHNICAL_SKILLS[1]),
        "skill_3": escape_html(settings.TECHNICAL_SKILLS[2]),
        "skill_4": escape_html(settings.TECHNICAL_SKILLS[3]),
    }

    return template_content.format(**sanitized_data)


def save_file(content: str, filename: str):
    """
    Writes the content to a file

    Args:
        content (str): content to write to the file
        filename (str): name of the file to write the content to
    """
    with open(filename, "w") as file:
        file.write(content)


if __name__ == "__main__":
    try:
        filename = parse_argument()
        template_content = read_template(filename)
        html_content = render_template(template_content)
        save_file(html_content, "myCV.html")

    except (ValueError, AssertionError) as e:
        print(f"Error parsing arguments: {e}", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error saving {filename}: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
