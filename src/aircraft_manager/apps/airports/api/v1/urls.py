from django.urls import path

from aircraft_manager.apps.airports.api.v1.views import AirportListAPIView

urlpatterns = [
    path("", AirportListAPIView.as_view(), name="list"),
]
