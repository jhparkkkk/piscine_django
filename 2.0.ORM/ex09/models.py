from django.db import models
from django.utils.timezone import now


class Planets(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    climate = models.CharField(
        max_length=128, null=True, blank=True, default="")
    diameter = models.IntegerField(null=True, blank=True, default=0)
    orbital_period = models.IntegerField(null=True, blank=True, default=0)
    population = models.BigIntegerField(null=True, blank=True, default=0)
    rotation_period = models.IntegerField(null=True, blank=True, default=0)
    surface_water = models.FloatField(null=True, blank=True, default=0)
    terrain = models.CharField(
        max_length=128, null=True, blank=True, default="")
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    birth_year = models.CharField(
        max_length=32, null=True, blank=True, default="")
    gender = models.CharField(max_length=32, null=True, blank=True, default="")
    eye_color = models.CharField(
        max_length=32, null=True, blank=True, default="")
    hair_color = models.CharField(
        max_length=32, null=True, blank=True, default="")
    height = models.IntegerField(null=True, blank=True, default=0)
    mass = models.FloatField(null=True, blank=True, default=0)
    homeworld = models.ForeignKey(
        Planets, on_delete=models.CASCADE, null=True, blank=True)  # ✅ Correction ici
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
