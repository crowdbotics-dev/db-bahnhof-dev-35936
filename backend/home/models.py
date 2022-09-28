from django.conf import settings
from django.db import models


class Location(models.Model):
    "Generated Model"
    lat = models.FloatField()
    lng = models.FloatField()
    name = models.CharField(
        max_length=256,
    )
