import copy

import pytest
from django.urls import reverse
from rest_framework import status

from aircraft_manager.apps.flights.models import Flight

pytestmark = pytest.mark.django_db


def test_flight_form_api_schema_get_success(api_client, flight_schema):
    client = api_client()
    response = client.get(reverse("api-v1-flights:form_schema"))
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == flight_schema


def test_flight_form_api_create_success(
    api_client, flight_create_data, aircraft, airport
):
    assert Flight.objects.count() == 0
    client = api_client()
    departure_airport = airport()
    arrival_airport = airport()
    aircraft = aircraft()
    data = copy.deepcopy(flight_create_data)
    data["departure_airport"] = str(departure_airport.id)
    data["arrival_airport"] = str(arrival_airport.id)
    data["aircraft"] = str(aircraft.id)
    response = client.post(
        reverse("api-v1-flights:form_schema"), data=data, format="json"
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert Flight.objects.count() == 1
