from django.shortcuts import render
from django.http import HttpResponse


def markdown_cheatsheet_view(request):
    return render(request, "index.html")
