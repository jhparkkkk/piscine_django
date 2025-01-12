from django.shortcuts import render, redirect
from ex05.views import Ex05MoviesViews
from ex07.models import Movies
from django.http import HttpResponse
from pathlib import Path

path = Path(__file__).resolve().parent.parent


class Ex07MoviesViews(Ex05MoviesViews):
    def update(self, request):
        try:
            if request.method == 'POST':
                movie_id = request.POST.get('id')
                new_opening_crawl = request.POST.get('opening_crawl')

                if movie_id and new_opening_crawl:
                    movie = Movies.objects.get(episode_nb=movie_id)
                    movie.opening_crawl = new_opening_crawl
                    movie.save()
                    return redirect('ex07_update')

            movies = Movies.objects.all().values()
            movies_list = [list(movie.values()) for movie in movies]
            if not movies:
                return HttpResponse("No data available")
            return render(request, f'{path}/ex06/templates/update_movie.html', {'movies': movies_list})
        except Exception as e:
            return HttpResponse(f"Error updating Movies: {e}")
