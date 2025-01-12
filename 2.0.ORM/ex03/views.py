from django.shortcuts import render
from django.http import HttpResponse
from utils.load_data import load_movies
from ex07.models import Movies
from pathlib import Path
from shared.views import MoviesViews

path = Path(__file__).resolve().parent.parent


class Ex03MoviesViews(MoviesViews):
    def populate(self, request):
        try:
            res = []
            movies = load_movies()
            for movie in movies:
                if not Movies.objects.filter(episode_nb=movie['episode_nb']).exists():
                    Movies.objects.create(**movie)
                    res.append('OK')
            response_html = "<br>".join(res)
            print(response_html)
            return HttpResponse(response_html)

        except Exception as e:
            return HttpResponse(f'Error populating {self.table_name}s: {e}')

    def display(self, request):
        try:
            movies = Movies.objects.all().values()
            movies_list = [list(movie.values()) for movie in movies]
            if not movies_list:
                return render(request, "no data available")

            raw_columns = movies[0].keys()
            columns = [column.replace('_', ' ').title()
                       for column in raw_columns]
            return render(request, f'{path}/ex02/templates/movies.html', {'movies': movies_list, 'columns': columns})
        except Exception as e:
            return HttpResponse(f"No data available: {str(e)}")
