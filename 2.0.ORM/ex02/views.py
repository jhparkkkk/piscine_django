from ex00.views import Ex00MoviesViews

from django.shortcuts import render
from django.http import HttpResponse
from utils.SQLDatabaseManager import DatabaseManager
from utils.load_data import load_movies
from pathlib import Path


class Ex02MoviesViews(Ex00MoviesViews):
    def populate(self, request):
        try:
            data = load_movies()
            db_manager = DatabaseManager()
            res = []
            for movie in data:
                try:
                    db_manager.insert(self.table_name, **movie)
                    res.append('OK')
                    print(f"movie {movie['title']
                                   } has been added to table ex02_movies.")
                except Exception as e:
                    continue

            response_html = "<br>".join(res)
            return HttpResponse(response_html)
        except Exception as e:
            return HttpResponse(f'Error populating {self.table_name}: {e}')

    def display(self, request):
        try:
            db_manager = DatabaseManager()
            movies = db_manager.select(self.table_name, '*')
            columns = ['Episode nb', 'Title', 'Opening_crawl', 'Director',
                       'Producer', 'Release Date', 'Created', 'Updated']
            return render(request, 'movies.html', {'movies':  movies, 'columns': columns})
        except Exception as e:
            return HttpResponse(f'Error displaying {self.table_name}: {e}')
