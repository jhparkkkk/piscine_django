from django.shortcuts import render

# Create your views here.
# ex00/views.py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Bienvenue dans l'application ex00!")


def markdown_cheatsheet_view(request):
    return render(request, "index.html")
