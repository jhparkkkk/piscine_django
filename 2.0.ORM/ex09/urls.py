from .views import Ex09Views
from utils.generate_urls import generate_urls


name = 'ex09'
actions = ['display']

urlpatterns = generate_urls(Ex09Views, name, actions)
