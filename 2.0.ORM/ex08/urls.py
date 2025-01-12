from .views import Ex08Views
from utils.generate_urls import generate_urls


name = 'ex08'

actions = ['init', 'populate', 'display']

urlpatterns = generate_urls(Ex08Views, name, actions)
