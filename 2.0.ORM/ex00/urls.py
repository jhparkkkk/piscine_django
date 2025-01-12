from .views import Ex00MoviesViews
from utils.generate_urls import generate_urls


name = 'ex00'
actions = ['init']

urlpatterns = generate_urls(Ex00MoviesViews, name, actions)
