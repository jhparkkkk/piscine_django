def get_list() -> list:
    """
    key: musician
    value: birth date
    Returns:
        list: list of tuples
    """
    return [
        ("Hendrix", "1942"),
        ("Allman", "1946"),
        ("King", "1925"),
        ("Clapton", "1945"),
        ("Johnson", "1911"),
        ("Berry", "1926"),
        ("Vaughan", "1954"),
        ("Cooder", "1947"),
        ("Page", "1944"),
        ("Richards", "1943"),
        ("Hammett", "1962"),
        ("Cobain", "1967"),
        ("Garcia", "1942"),
        ("Beck", "1944"),
        ("Santana", "1947"),
        ("Ramone", "1948"),
        ("White", "1975"),
        ("Frusciante", "1970"),
        ("Thompson", "1949"),
        ("Burton", "1939"),
    ]


def convert(my_list: list, my_dict: dict) -> dict:
    """
    Convert a list of tuples into a dictionary.

    Args:
        my_list (list): the list to convert
        my_dict (dict): the dictionary to create

    Returns:
        dict: the dictionary created from the converted list
    """
    for key, value in my_list:
        my_dict.setdefault(value, []).append(key)
    return my_dict


def print_dict(my_dict: dict):
    """
    Prints the dictionary with the key (birth year) followed by the names

    Args:
        my_dict (dict): object to print
    """
    for key, value in my_dict.items():
        print(f"{key} : {', '.join(value)}")


if __name__ == "__main__":
    try:
        # create a dictionary and a list
        my_dict = {}
        my_list = get_list()

        # convert list into dict
        my_dict = convert(my_list, my_dict)

        # display
        print_dict(my_dict)
    except Exception as error:
        print(error)
