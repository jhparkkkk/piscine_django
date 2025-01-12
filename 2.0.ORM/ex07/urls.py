from .views import Ex07MoviesViews
from utils.generate_urls import generate_urls


name = 'ex07'

actions = ['populate', 'display', 'update']

urlpatterns = generate_urls(Ex07MoviesViews, name, actions)
