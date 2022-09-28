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


class VehicleSchedule(models.Model):
    "Generated Model"
    vehicle_id = models.ForeignKey(
        "home.Vehicle",
        on_delete=models.CASCADE,
        blank=True,
        related_name="vehicleschedule_vehicle_id",
    )
    start_time = models.DateTimeField(
        blank=True,
    )
    from_location = models.ForeignKey(
        "home.Location",
        on_delete=models.CASCADE,
        blank=True,
        related_name="vehicleschedule_from_location",
    )
    to_location = models.ForeignKey(
        "home.Location",
        on_delete=models.CASCADE,
        blank=True,
        related_name="vehicleschedule_to_location",
    )
    end_time = models.DateTimeField(
        blank=True,
    )
