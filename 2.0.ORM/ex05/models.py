from shared.models import BaseMoviesModel
from django.db import models


class Movies(BaseMoviesModel):
    class Meta:
        app_label = "ex05"
