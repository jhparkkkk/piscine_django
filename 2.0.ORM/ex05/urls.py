from .views import Ex05MoviesViews
from utils.generate_urls import generate_urls


name = 'ex05'
actions = ['populate', 'display', 'remove']

urlpatterns = generate_urls(Ex05MoviesViews, name, actions)
