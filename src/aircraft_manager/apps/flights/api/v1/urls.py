from django.urls import path

from aircraft_manager.apps.flights.api.v1.views import (
    FlightListAPIView,
    FlightFormAPIView,
)

urlpatterns = [
    path("", FlightListAPIView.as_view(), name="list"),
    path(
        "form-schema/",
        FlightFormAPIView.as_view(),
        name="form_schema",
    ),
]
