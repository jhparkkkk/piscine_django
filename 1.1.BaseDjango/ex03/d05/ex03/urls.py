from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='ex03_index'),
]
