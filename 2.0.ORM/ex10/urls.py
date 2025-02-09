from django.urls import path
from .views import Ex10Views
from utils.generate_urls import generate_urls

name = 'ex10'
actions = ['movie_search']

urlpatterns = generate_urls(Ex10Views, name, actions)
