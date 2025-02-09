from django.shortcuts import render
from pathlib import Path
from django.views import View
from shared.views import MoviesViews
from ex09.models import People

path = Path(__file__).resolve().parent.parent


class Ex09Views(MoviesViews):
    def display(self, request):
        characters = People.objects.filter(
            homeworld__climate__icontains="windy").order_by("name")

        if not characters.exists():
            return render(request, f'{path}/ex09/templates/planets_people.html', {
                "message": "No data available, please use the following command line before use:",
                "command": "python manage.py loaddata data/ex09_initial_data.json"
            })

        return render(request, f'{path}/ex09/templates/planets_people.html', {"characters": characters})
