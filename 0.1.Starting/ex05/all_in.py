import sys


def get_states() -> dict:
    """
    Returns a dictionary mapping U.S. state names to their postal codes.

    Returns:
        dict: a dictionary with state names as keys and postal codes as values
    """
    return {"Oregon": "OR",
            "Alabama": "AL",
            "New Jersey": "NJ",
            "Colorado": "CO"}


def get_capital_cities() -> dict:
    """
    Returns a dictionary mapping U.S. postal codes to their capital cities.

    Returns:
        dict: a dictionary with postal codes as keys
              and capital cities as values
    """
    return {"OR": "Salem",
            "AL": "Montgomery",
            "NJ": "Trenton",
            "CO": "Denver"}


def preprocess_data(
    raw_input: str, states: dict, capital_cities: dict
) -> tuple[list, dict, dict]:
    """
    Normalizes and prepares raw input data and dictionaries.

    Args:
        raw_input (str): User input, words separated by commas.
        states (dict): dictionary of state names to their postal codes.
        capital_cities (dict): dictionary of postal codes to capital city names

    Returns:
        tuple: tuple containing a list of
                - cleaned input
                - and normalized dictionaries.
    """
    states = {k.lower(): v for k, v in states.items()}
    capital_cities = {k: v.lower() for k, v in capital_cities.items()}

    raw_input = raw_input.split(", ")
    raw_input = [item.strip() for item in raw_input if item]
    
    if  len(raw_input[0]) == 0:
        raise ValueError()

    return raw_input, states, capital_cities


def find_successive_commas(user_input: str) -> bool:
    """
    Checks for successive commas in user input

    Args:
        user_input (str): input string to check

    Returns:
        bool: True if successive commas are found, False otherwise
    """
    return ",," in user_input


def search_state(states: dict, capital_cities: dict, query: str) -> str:
    """
    Finds the state corresponding to a given capital city query

    Args:
        states (dict): _description_
        capital_cities (dict): _description_
        query (str): _description_

    Returns:
        str: _description_
    """
    postal_code = list(capital_cities.keys())[
        list(capital_cities.values()).index(query)
    ]
    return list(states.keys())[list(states.values()).index(postal_code)]


def print_result(state: str, capital_city: str):
    """
    Prints the search result

    Args:
        state (str): the state name or the original query if not found
        capital_city (str): capital city name if found
    """
    if capital_city:
        print(f"{capital_city.capitalize()} is the capital of {state.title()}")
    else:
        print(f"{state} is neither a capital city nor a state")


def resolve_queries(queries: list, states: dict, capital_cities: dict):
    """
    Processes each query by checking if it is a state or capital city.
    - If query is a capital city, search for its state.
    - If query is a state, search for its capital city.

    Args:
        queries (list): list of queries to process
        states (dict): dictionary of states and postal codes
        capital_cities (dict): dictionary of postal codes and states
    """
    for i, query in enumerate(queries):
        try:
            query = query.lower()
            if query in states:
                print_result(query, capital_cities[states[query]])
            elif query in capital_cities.values():
                print_result(search_state(states, capital_cities, query),
                             query)
            else:
                print_result(queries[i], None)
        except Exception:
            print_result(queries[i], None)


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2, "Only 1 argument required"
        assert not find_successive_commas(sys.argv[1])

        states = get_states()
        capital_cities = get_capital_cities()

        queries, states_copy, capital_cities_copy = preprocess_data(
            sys.argv[1], get_states(), get_capital_cities()
        )

        resolve_queries(queries, states_copy, capital_cities_copy)

    except Exception:
        exit(1)
