from django import forms
from django.shortcuts import render
from pathlib import Path
from shared.views import MoviesViews
from ex10.models import People
from django.db import connection
path = Path(__file__).resolve().parent.parent


def get_gender_choices():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT to_regclass('ex10_people');"
        )
        table_exists = cursor.fetchone()[0] is not None

    if table_exists:
        return People.objects.values_list("gender", "gender").distinct()
    return []


class MovieSearchForm(forms.Form):
    min_release_date = forms.DateField(
        label="Movies minimum release date", widget=forms.DateInput(attrs={'type': 'date'}))
    max_release_date = forms.DateField(
        label="Movies maximum release date", widget=forms.DateInput(attrs={'type': 'date'}))
    min_diameter = forms.IntegerField(
        label="Planet diameter greater than", min_value=0)

    gender_choices = get_gender_choices()
    gender = forms.ChoiceField(
        label="Character gender", choices=gender_choices)


class Ex10Views(MoviesViews):
    def movie_search(self, request):
        if 'ex10_people' not in connection.introspection.table_names():
            return render(request, 'error.html', {'message': 'Table ex10_people does not exist'})
        form = MovieSearchForm(request.GET or None)
        results = []
        if form.is_valid():
            min_date = form.cleaned_data["min_release_date"]
            max_date = form.cleaned_data["max_release_date"]
            min_diameter = form.cleaned_data["min_diameter"]
            gender = form.cleaned_data["gender"]

            results = (
                People.objects.filter(
                    gender=gender,
                    movies__release_date__range=(min_date, max_date),
                    homeworld__diameter__gte=min_diameter
                )
                .values_list("movies__title", "name", "gender", "homeworld__name", "homeworld__diameter")
                .order_by("name")
            )
            print(f"Results: {list(results)}")
        return render(request, f"{path}/ex10/templates/search_results.html", {"form": form, "results": results})
