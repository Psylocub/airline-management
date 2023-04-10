from django_filters.filters import CharFilter
from django_filters.rest_framework.filterset import FilterSet

from aircraft_manager.apps.airports.models import Airport


class AirportFilterSet(FilterSet):
    manufacturer = CharFilter(
        field_name="icao_code",
        help_text="ICAO code of airport",
        lookup_expr="exact",
    )
    serial_number = CharFilter(
        field_name="country",
        help_text="Country of airport",
        lookup_expr="exact",
    )

    class Meta:
        model = Airport
        fields = (
            "icao_code",
            "country",
        )
