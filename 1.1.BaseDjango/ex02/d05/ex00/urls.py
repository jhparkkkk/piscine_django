from django.urls import path
from . import views

urlpatterns = [
    path('', views.markdown_cheatsheet_view, name='ex00_index'),
]
