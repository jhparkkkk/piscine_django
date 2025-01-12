from .views import Ex02MoviesViews
from utils.generate_urls import generate_urls

name = 'ex02'
actions = ['init', 'populate', 'display']

urlpatterns = generate_urls(Ex02MoviesViews, name, actions)
