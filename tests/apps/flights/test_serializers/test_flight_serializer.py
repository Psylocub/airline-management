import pytest

from aircraft_manager.apps.flights.api.v1.serializers import FlightListSerializer
from aircraft_manager.apps.flights.models import Flight


@pytest.mark.django_db
def test_flight_list_serializer(aircraft, airport):
    departure_airport = airport()
    arrival_airport = airport()
    aircraft = aircraft()
    departure_airport.icao_code = "GETV"
    arrival_airport.icao_code = "BURW"
    aircraft.serial_number = "1234"
    flight = Flight.objects.create(
        departure_airport=departure_airport,
        departure_date="2024-02-15 11:15",
        arrival_airport=arrival_airport,
        arrival_date="2024-03-15 11:15",
        aircraft=aircraft,
    )
    serializer = FlightListSerializer(flight)
    expected_data = {
        "id": str(flight.id),
        "departure_airport": "GETV",
        "departure_date": "2024-02-15 11:15",
        "arrival_airport": "BURW",
        "arrival_date": "2024-03-15 11:15",
        "aircraft": "1234",
    }
    assert serializer.data == expected_data
