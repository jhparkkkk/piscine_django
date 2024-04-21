import sys


def get_states() -> dict:
    """
    Returns a dictionary mapping U.S. state names to their postal codes.

    Returns:
        dict: a dictionary with state names as keys and postal codes as values
    """
    return {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}


def get_capital_cities() -> dict:
    """
    Returns a dictionary mapping U.S. postal codes to their capital cities.

    Returns:
        dict: a dictionary with postal codes as keys and capital cities as values
    """
    return {"OR": "Salem", "AL": "Montgomery", "NJ": "Trenton", "CO": "Denver"}


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2, "Only 1 argument required."

        states = get_states()
        capital_cities = get_capital_cities()

        print(capital_cities[states[sys.argv[1]]])

    except KeyError as error:
        print("Unknown state", file=sys.stderr)
    except Exception as error:
        exit(1)
