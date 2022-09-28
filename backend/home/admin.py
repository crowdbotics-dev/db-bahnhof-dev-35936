from django.contrib import admin
from .models import Location, Vehicle, VehicleSchedule

admin.site.register(Location)
admin.site.register(Vehicle)
admin.site.register(VehicleSchedule)

# Register your models here.
