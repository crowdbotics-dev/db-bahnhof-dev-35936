from django.conf import settings
from django.db import models


class Location(models.Model):
    "Generated Model"
    lat = models.FloatField()
    lng = models.FloatField()
    name = models.CharField(
        max_length=256,
    )


class Vehicle(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    code = models.SlugField(
        max_length=50,
    )
    license_plate = models.CharField(
        max_length=256,
    )
    capacity = models.IntegerField()
    type = models.CharField(
        max_length=256,
    )
