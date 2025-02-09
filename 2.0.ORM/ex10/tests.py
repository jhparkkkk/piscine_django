from django.db import models
from django.utils.timezone import now


class Planets(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    climate = models.TextField(null=True, blank=True)
    diameter = models.IntegerField(null=True, blank=True)
    orbital_period = models.IntegerField(null=True, blank=True)
    population = models.BigIntegerField(null=True, blank=True)
    rotation_period = models.IntegerField(null=True, blank=True)
    surface_water = models.FloatField(null=True, blank=True)
    terrain = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    birth_year = models.CharField(max_length=32, null=True, blank=True)
    gender = models.CharField(max_length=32)
    eye_color = models.CharField(max_length=32, null=True, blank=True)
    hair_color = models.CharField(max_length=32, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    mass = models.FloatField(null=True, blank=True)
    homeworld = models.ForeignKey(
        Planets, on_delete=models.SET_NULL, null=True, blank=True
    )
    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True, null=False)
    release_date = models.DateField(null=True, blank=True)
    director = models.CharField(max_length=64, null=True, blank=True)
    producer = models.CharField(max_length=128, null=True, blank=True)
    characters = models.ManyToManyField(People, related_name="movies")
    created = models.DateTimeField(
        default=now, editable=False)  # Ajout cohérent

    def __str__(self):
        return self.title
