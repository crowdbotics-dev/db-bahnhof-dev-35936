from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import LocationViewSet, VehicleViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("location", LocationViewSet)
router.register("vehicle", VehicleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
