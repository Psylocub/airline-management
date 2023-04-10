from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import F

from aircraft_manager.apps.core.models import CoreModel


class Airport(CoreModel):
    icao_code = models.CharField(
        max_length=4,
        unique=True,
        validators=[MinLengthValidator(4)],
        help_text="Airport location indicator code designating aerodromes around the world",
    )
    country = models.CharField(max_length=100, help_text="Country of airport")

    def __str__(self):
        return self.icao_code

    @classmethod
    def get_choices_dict(cls):
        return list(
            cls.objects.active()
            .order_by("icao_code")
            .values(
                display_name=F("icao_code"),
                value=F("id"),
            )
        )
