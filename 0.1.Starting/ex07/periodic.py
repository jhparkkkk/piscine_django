NB_ROW = 7
NB_COL = 18

def read_periodic_table(filepath: str):
    elements = {}
    row = 0
    with open(filepath, "r") as f:
        for line in f:
            parts = line.strip().split(", ")
            name = parts[0].split(" = ")
            position = parts[0].split(":")
            number = parts[1].split(":")
            small = parts[2].split(": ")
            molar = parts[3].split(":")
            electron = parts[4].split(":")

            elements[int(number[1])] = {
                "name": name[0],
                "position": int(position[1]),
                "row": row,
                number[0]: int(number[1]),
                small[0]: small[1],
                molar[0]: molar[1],
                electron[0]: electron[1],
            }

            if int(position[1]) == NB_COL - 1:
                row += 1

    return elements


def create_cell(element):
    cell = f"""<td class="element-cell">
            <h4>{element['small']}</h4>
            <ul>
                <li>{element['number']}</li>
                <li>{element['name']}</li>
                <li>{element['molar']}</li>
                <li>{element['electron']}</li>
            </ul>
        </td>\n"""
    return cell


def create_empty_cell():
    return f"""<td class="empty-cell">
        </td>"""


def search_by_position_and_row(elements, position, row):
    results = {}
    for key, element in elements.items():
        if element["position"] == position and element["row"] == row:
            return key
    return None


def create_row(elements: dict, row_idx: int):
    row = f"<tr>\n"
    for col_idx in range(0, NB_COL):
        key = search_by_position_and_row(elements, col_idx, row_idx)
        if key:
            row += create_cell(elements[key])
        else:
            row += create_empty_cell()

    row += f"</tr>\n"
    return row


def create_html(elements: dict):
    content = """<!DOCTYPE html>

<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Periodic Table</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
  <table>\n"""

    for row_nb in range(0, NB_ROW):
        content += create_row(elements, row_nb)

    content += """  \n  </table>
  </body>
</html>"""

    return content


def save_file(content: str, filename: str):
    with open(filename, "w") as file:
        file.write(content)


def create_css(elements: dict):
    content = """

body {
    font-family: 'Arial', sans-serif;
    background-color: #f4f4f4;
    margin: 2rem;
}

table {
    width: 100%;
    border-collapse: separate;
    table-layout: fixed; 
}

td {
    width: 6rem;
    height: 6rem;
    text-align: center;
    vertical-align: middle;
    background-color: white;
    box-sizing: border-box;
    border-radius: 0.9rem;
    border: 1px solid black;

}

h4, ul, li {
    margin: 0;
    padding: 0;
    line-height: normal;
}

h4 {
    font-size: 1.5rem;
    font-weight: 1000;
}

ul {
    list-style-type: none;
}

li {
    font-size: 0.8rem;
    color: rgb(98, 98, 98);
    line-height: 1rem;
}

.empty-cell {
    background-color: transparent; 
    border: none;
}

.element-cell {
    padding: 0.3rem;
}
"""
    return content


if __name__ == "__main__":
    try:
        elements = read_periodic_table("periodic_table.txt")

        assert len(elements) != 0, "Could not retrieve periodic table data"
        html_content = create_html(elements)
        save_file(html_content, "periodic_table.html")

        css_content = create_css(elements)
        save_file(css_content, "style.css")
    except Exception as error:
        print(f"Error: {error}")
        exit(1)
