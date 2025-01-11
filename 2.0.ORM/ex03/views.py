from django.shortcuts import render
from django.http import HttpResponse
from utils.load_data import load_movies
from ex03.models import Movies
from pathlib import Path

path = Path(__file__).resolve().parent.parent


def populate(request):
    try:
        res = []
        movies = load_movies()
        for movie in movies:
            Movies.objects.create(**movie)
            res.append('OK')
        return HttpResponse('OK')

    except Exception as e:
        return HttpResponse(f'Error populating ex02_movies: {e}')


def display(request):
    try:
        movies = Movies.objects.all()
        movies_list = [(movie.episode_nb, movie.title, movie.opening_crawl,
                        movie.director, movie.producer, movie.release_date) for movie in movies]
        if not movies_list:
            return render(request, "no data available")
        return render(request, f'{path}/ex02/templates/movies.html', {'movies': movies_list})
    except Exception as e:
        return HttpResponse(f"No data available: {str(e)}")
