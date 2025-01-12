from .views import Ex06MoviesViews
from utils.generate_urls import generate_urls


name = 'ex06'
actions = ['init', 'populate', 'display', 'update']

urlpatterns = generate_urls(Ex06MoviesViews, name, actions)
