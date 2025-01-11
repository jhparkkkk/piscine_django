from django.shortcuts import render
from django.http import HttpResponse
from utils.SQLDatabaseManager import DatabaseManager
from utils.load_data import load_movies
from pathlib import Path


def init(request):
    try:
        db_manager = DatabaseManager()
        db_manager.create_table('ex02_movies')
        db_manager.get_all_tables()
        return HttpResponse('OK')
    except Exception as e:
        return HttpResponse(f'Error creating ex02_movies: {e}')


def populate(request):
    try:
        data = load_movies()
        db_manager = DatabaseManager()
        db_manager.drop_table('ex02_movies')
        db_manager.create_table('ex02_movies')
        res = []
        for movie in data:
            db_manager.insert('ex02_movies', **movie)
            res.append('OK')
            print(f"movie {movie['title']
                           } has been added to table ex02_movies.")

        response_html = "<br>".join(res)
        return HttpResponse(response_html)
    except Exception as e:
        return HttpResponse(f'Error populating ex02_movies: {e}')


def display(request):
    try:
        db_manager = DatabaseManager()
        movies = db_manager.select('ex02_movies', '*')
        return render(request, 'movies.html', {'movies':  movies})
    except Exception as e:
        return HttpResponse(f'Error displaying ex02_movies: {e}')
