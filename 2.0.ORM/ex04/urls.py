from .views import Ex04MoviesViews
from utils.generate_urls import generate_urls


name = 'ex04'
actions = ['init', 'populate', 'display', 'remove']

urlpatterns = generate_urls(Ex04MoviesViews, name, actions)
