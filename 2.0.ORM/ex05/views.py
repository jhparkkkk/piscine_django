from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from utils.load_data import load_movies
from ex05.models import Movies
from pathlib import Path
from ex03.views import Ex03MoviesViews
path = Path(__file__).resolve().parent.parent


class Ex05MoviesViews(Ex03MoviesViews):
    def populate(self, request):
        return super().populate(request)

    def display(self, request):
        return super().display(request)

    def remove(self, request):
        try:
            if request.method == 'POST':
                movie_id = request.POST.get('id')
                if movie_id:
                    Movies.objects.filter(episode_nb=movie_id).delete()
                    return redirect(f"/{self.table_name.split('_')[0]}/remove")
            movies = Movies.objects.all()
            movies_list = [(movie.episode_nb, movie.title, movie.opening_crawl,
                            movie.director, movie.producer, movie.release_date) for movie in movies]
            return render(request, f'{path}/ex04/templates/remove_movie.html', {'movies': movies_list})
        except Exception as e:
            return HttpResponse(f'Error removing ex05_movies: {e}')
