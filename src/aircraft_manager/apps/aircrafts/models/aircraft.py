from django.db import models
from django.db.models import F

from aircraft_manager.apps.core.models import CoreModel


class Aircraft(CoreModel):
    serial_number = models.CharField(
        max_length=36, unique=True, help_text="Aircraft unique serial number"
    )
    manufacturer = models.CharField(
        max_length=255, help_text="Aircraft manufacturer company name"
    )

    def __str__(self):
        return f"{self.manufacturer} #{self.serial_number}"

    @classmethod
    def get_choices_dict(cls):
        return list(
            cls.objects.active()
            .order_by("serial_number")
            .values(
                display_name=F("serial_number"),
                value=F("id"),
            )
        )
