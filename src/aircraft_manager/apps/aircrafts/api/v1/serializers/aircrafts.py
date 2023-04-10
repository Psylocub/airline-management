from rest_framework import serializers

from aircraft_manager.apps.aircrafts.models import Aircraft


class AircraftListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = (
            "id",
            "manufacturer",
            "serial_number",
        )
