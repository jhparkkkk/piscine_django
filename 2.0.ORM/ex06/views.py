from django.shortcuts import render, redirect
from utils.SQLDatabaseManager import DatabaseManager
from django.http import HttpResponse
from utils.load_data import load_movies
from ex04.views import Ex04MoviesViews


class Ex06MoviesViews(Ex04MoviesViews):
    def init(self, request):
        super().init(request)
        try:
            db_manager = DatabaseManager()
            db_manager.alter_table(self.table_name, 'created',
                                   'TIMESTAMP', 'DEFAULT CURRENT_TIMESTAMP', 'NOT NULL')
            db_manager.alter_table(self.table_name, 'updated', 'TIMESTAMP',
                                   'DEFAULT CURRENT_TIMESTAMP', 'NOT NULL')
            db_manager.create_trigger(
                self.table_name, 'update_films_changetimestamp', 'update_changetimestamp_column')
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse(f'Error initializing {self.table_name}: {e}')

    def update(self, request):
        try:
            if request.method == 'POST':
                movie_id = request.POST.get('id')
                new_opening_crawl = request.POST.get('opening_crawl')

                if movie_id and new_opening_crawl:
                    db_manager = DatabaseManager()
                    db_manager.update(self.table_name, 'episode_nb', movie_id, {
                                      'opening_crawl': new_opening_crawl})
                    return redirect('ex06_update')

            db_manager = DatabaseManager()
            movies = db_manager.select(self.table_name, '*')

            return render(request, f'update_movie.html', {'movies':  movies})
        except Exception as e:
            return HttpResponse(f'Error updating {self.table_name}: {e}')
