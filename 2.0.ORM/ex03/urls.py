from .views import Ex03MoviesViews
from utils.generate_urls import generate_urls

name = 'ex03'
actions = ['populate', 'display']

urlpatterns = generate_urls(Ex03MoviesViews, name, actions)
