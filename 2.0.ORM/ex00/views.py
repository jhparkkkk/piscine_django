from shared.views import MoviesViews
from utils.SQLDatabaseManager import DatabaseManager
from django.http import HttpResponse


class Ex00MoviesViews(MoviesViews):

    def init(self, request):
        try:
            db_manager = DatabaseManager()
            db_manager.create_table(self.table_name)
            db_manager.get_all_tables()
            db_manager.disconnect()
            return HttpResponse('OK')
        except Exception as e:
            return HttpResponse(f'Error creating {self.table_name}: {e}')
