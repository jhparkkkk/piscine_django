from django.shortcuts import render, redirect
from django.http import HttpResponse
from utils.load_data import load_movies
from utils.SQLDatabaseManager import DatabaseManager
from pathlib import Path
from ex02.views import Ex02MoviesViews

path = Path(__file__).resolve().parent


class Ex04MoviesViews(Ex02MoviesViews):
    def remove(self, request):
        try:
            db_manager = DatabaseManager()

            if request.method == 'POST':
                print(self.table_name.split('_')[0])

                movie_id = request.POST.get('id')
                if movie_id:
                    db_manager.delete(self.table_name, 'episode_nb', movie_id)
                    return redirect(f"/{self.table_name.split('_')[0]}/remove")
            movies = db_manager.select(self.table_name, '*')
            print(self.table_name.split('_')[0] + "_remove")
            redirect_url = f"{
                self.table_name.split('_')[0]}_remove"
            print(redirect_url)
            return render(request, f'remove_movie.html', {'movies':  movies,
                                                          'url': redirect_url})
        except Exception as e:
            return HttpResponse(f'Error removing {self.table_name}: {e}')
