from rest_framework import serializers

from aircraft_manager.apps.airports.models import Airport


class AirportListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = (
            "id",
            "icao_code",
            "country",
        )
