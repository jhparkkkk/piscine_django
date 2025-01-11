from django.urls import path
from . import views

urlpatterns = [
    path('populate/', views.populate, name='populate_movie_table'),
    path('display/', views.display, name='display_movie_table'),

]
