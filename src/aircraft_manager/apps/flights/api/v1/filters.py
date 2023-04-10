from django_filters.filters import CharFilter, DateFilter
from django_filters.rest_framework.filterset import FilterSet

from aircraft_manager.apps.flights.models import Flight


class FlightFilterSet(FilterSet):
    departure_airport = CharFilter(
        field_name="departure_airport__icao_code",
        help_text="ICAO code",
        lookup_expr="exact",
    )
    arrival_airport = CharFilter(
        field_name="arrival_airport__icao_code",
        help_text="ICAO code",
        lookup_expr="exact",
    )
    flight_date_start = DateFilter(
        field_name="departure_date",
        help_text="YYYY/MM/DD HH:MM",
        input_formats=["%Y/%m/%d %H:%M"],
        lookup_expr="gte",
    )
    flight_date_end = DateFilter(
        field_name="arrival_date",
        help_text="YYYY/MM/DD HH:MM",
        input_formats=["%Y/%m/%d %H:%M"],
        lookup_expr="lte",
    )

    class Meta:
        model = Flight
        fields = (
            "departure_airport",
            "arrival_airport",
            "flight_date_start",
            "flight_date_end",
        )
