from django.http import HttpResponse
from utils.SQLDatabaseManager import DatabaseManager
from django.views import View
from abc import ABC, abstractmethod


class MoviesViews(View, ABC):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.name = kwargs.get('name')
        self.table_name = f'{self.name}_movies'
        print('******** SETUP ********')
        print(self.table_name)
        print('******** SETUP ********')

    def get(self, request, *args, **kwargs):
        action = kwargs.get('action')
        if action and hasattr(self, action):
            action_method = getattr(self, action)
            return action_method(request)
        return HttpResponse("Action not supported")

    def post(self, request, *args, **kwargs):
        action = kwargs.get('action')
        if action and hasattr(self, action):
            action_method = getattr(self, action)
            return action_method(request)
        return HttpResponse("POST action not supported")

    def init(self, request):
        pass

    def populate(self, request):
        pass

    def display(self, request):
        pass

    def remove(self, request):
        pass

    def update(self, request):
        pass
