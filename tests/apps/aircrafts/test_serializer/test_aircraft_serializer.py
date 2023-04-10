import pytest

from aircraft_manager.apps.aircrafts.api.v1.serializers import AircraftListSerializers
from aircraft_manager.apps.aircrafts.models import Aircraft


@pytest.mark.django_db
def test_aircraft_list_serializer():
    aircraft = Aircraft.objects.create(manufacturer="Boeing", serial_number="1234")
    serializer = AircraftListSerializers(aircraft)
    expected_data = {
        "id": str(aircraft.id),
        "manufacturer": "Boeing",
        "serial_number": "1234",
    }
    assert serializer.data == expected_data
