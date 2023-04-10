from django_filters.filters import CharFilter
from django_filters.rest_framework.filterset import FilterSet

from aircraft_manager.apps.aircrafts.models import Aircraft


class AircraftFilterSet(FilterSet):
    manufacturer = CharFilter(
        field_name="manufacturer",
        help_text="Manufacturer of aircraft",
        lookup_expr="exact",
    )
    serial_number = CharFilter(
        field_name="serial_number",
        help_text="Serial number of aircraft",
        lookup_expr="exact",
    )

    class Meta:
        model = Aircraft
        fields = (
            "manufacturer",
            "serial_number",
        )
