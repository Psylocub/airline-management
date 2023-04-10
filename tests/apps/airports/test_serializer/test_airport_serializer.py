import pytest

from aircraft_manager.apps.airports.api.v1.serializers import AirportListSerializers
from aircraft_manager.apps.airports.models import Airport


@pytest.mark.django_db
def test_airport_list_serializer():
    airport = Airport.objects.create(icao_code="GETV", country="Germany")
    serializer = AirportListSerializers(airport)
    expected_data = {"id": str(airport.id), "icao_code": "GETV", "country": "Germany"}
    assert serializer.data == expected_data
