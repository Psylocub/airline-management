from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from aircraft_manager.apps.flights.models import Flight


class FlightListSerializer(serializers.ModelSerializer):
    departure_airport = serializers.CharField(source="departure_airport.icao_code")
    arrival_airport = serializers.CharField(source="arrival_airport.icao_code")
    departure_date = serializers.DateTimeField(format="%Y/%m/%d %H:%M")
    arrival_date = serializers.DateTimeField(format="%Y/%m/%d %H:%M")
    aircraft = serializers.SerializerMethodField()

    def get_aircraft(self, obj):
        if obj.aircraft:
            return obj.aircraft.serial_number
        else:
            return None

    class Meta:
        model = Flight
        fields = (
            "id",
            "departure_airport",
            "departure_date",
            "arrival_airport",
            "arrival_date",
            "aircraft",
        )


class FlightFormSerializer(serializers.ModelSerializer):
    departure_airport = serializers.UUIDField(source="departure_airport_id")
    arrival_airport = serializers.UUIDField(source="arrival_airport_id")
    aircraft = serializers.UUIDField(source="aircraft_id")

    class Meta:
        model = Flight
        fields = (
            "departure_airport",
            "departure_date",
            "arrival_airport",
            "arrival_date",
            "aircraft",
        )

    def validate(self, attrs):
        if (
            attrs.get("departure_date") < timezone.now()
            or attrs.get("arrival_date") < timezone.now()
        ):
            raise ValidationError(
                "A flight can not be created with departure date in the past"
            )
        if attrs.get("departure_airport_id") == attrs.get("arrival_airport_id"):
            raise ValidationError(
                "Departure airport and arrival airport can not be the same"
            )
        if attrs.get("departure_date") > attrs.get("arrival_date"):
            raise ValidationError("Arrival date can not be earlier than departure date")
        if Flight.objects.filter(
            aircraft__id=attrs.get("aircraft_id"), is_active=True
        ).exists():
            raise ValidationError("Chosen aircraft is already in use")
        return super().validate(attrs)
