from shared.models import BaseMoviesModel
from django.db import models
from datetime import datetime


class Movies(BaseMoviesModel):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "ex07"
