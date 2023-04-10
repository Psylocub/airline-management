from django.urls import path

from aircraft_manager.apps.aircrafts.api.v1.views import AircraftListAPIView

urlpatterns = [
    path("", AircraftListAPIView.as_view(), name="list"),
]
