import os
import json
MOVIES_FILE = os.path.join(os.path.dirname(__file__), '../data/movies.json')


def load_movies():
    try:
        with open(MOVIES_FILE, 'r') as file:
            return json.load(file)
    except Exception as e:
        raise (f'Error loading movies: {e}')
