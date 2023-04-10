from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from aircraft_manager.apps.aircrafts.models import Aircraft
from aircraft_manager.apps.airports.models import Airport
from aircraft_manager.apps.core.models import CoreModel


class Flight(CoreModel):
    departure_airport = models.ForeignKey(
        Airport, on_delete=models.PROTECT, related_name="departure_airport"
    )
    departure_date = models.DateTimeField()
    arrival_airport = models.ForeignKey(
        Airport, on_delete=models.PROTECT, related_name="arrival_airport"
    )
    arrival_date = models.DateTimeField()
    aircraft = models.ForeignKey(
        Aircraft, on_delete=models.PROTECT, null=True, blank=True
    )

    class Meta:
        unique_together = ("aircraft", "is_active")

    def __str__(self):
        if self.aircraft is None:
            aircraft = "NO AIRCRAFT FOR THIS FLIGHT"
        else:
            aircraft = f"{self.aircraft.manufacturer} #{self.aircraft.serial_number}"
        return (
            f"Flight {self.departure_airport} -> {self.arrival_airport} \
        |  {self.departure_date.strftime('%Y/%m/%d %H:%M')} -> {self.arrival_date.strftime('%Y/%m/%d %H:%M')} \
        | "
            + aircraft
        )

    def clean(self):
        if self.departure_date < timezone.now() or self.arrival_date < timezone.now():
            raise ValidationError(
                "A flight can not be created with departure date in the past"
            )
        if self.departure_airport == self.arrival_airport:
            raise ValidationError(
                "Departure airport and arrival airport can not be the same"
            )
        if self.departure_date > self.arrival_date:
            raise ValidationError("Arrival date can not be earlier than departure date")
        super().clean()
