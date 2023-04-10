import copy
import datetime

from django_filters.rest_framework.backends import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.views import Response

from aircraft_manager.apps.aircrafts.models import Aircraft
from aircraft_manager.apps.airports.models import Airport
from aircraft_manager.apps.flights.api.v1.filters import FlightFilterSet
from aircraft_manager.apps.flights.api.v1.serializers import (
    FlightListSerializer,
    FlightFormSerializer,
)
from aircraft_manager.apps.flights.models import Flight


@extend_schema(tags=["flights"])
class FlightListAPIView(ListAPIView):
    serializer_class = FlightListSerializer
    queryset = Flight.objects.all()
    filterset_class = FlightFilterSet
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    ordering_fields = (
        "departure_airport",
        "departure_date",
        "arrival_airport",
        "arrival_date",
        "aircraft",
    )
    ordering = ("-created",)
    search_fields = (
        "departure_airport__icao_code",
        "departure_date",
        "arrival_airport__icao_code",
        "arrival_date",
        "aircraft__serial_number",
    )

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if "sorted" not in request.GET.keys():
            return response
        data = copy.deepcopy(response.data)
        raw_results = data.pop("results", [])
        results = []
        flight = {}
        flights_count = 0
        if raw_results:
            sorted_raw_result = sorted(
                raw_results, key=lambda dictionary: dictionary["departure_airport"]
            )
            for item in sorted_raw_result:
                departure_airport = item.get("departure_airport")
                if flight and flight.get("Departure airport") != departure_airport:
                    flight = {}
                    flights_count = 0
                    flight["Departure airport"] = departure_airport
                    flight["Number of flights"] = flights_count
                    results.append(flight)
                elif not flight:
                    flight["Departure airport"] = departure_airport
                    results.append(flight)
                aircraft = item.get("aircraft")
                start_time = item.get("departure_date")
                end_time = item.get("arrival_date")
                in_flight_time = self.time_difference(start_time, end_time)
                flight[f"Aircraft: {aircraft}"] = in_flight_time
                flights_count += 1
                flight["Number of flights"] = flights_count
        return Response(results)

    @staticmethod
    def time_difference(departure_time, arrival_time):
        arrival = datetime.datetime.strptime(arrival_time, "%Y/%m/%d %H:%M")
        departure = datetime.datetime.strptime(departure_time, "%Y/%m/%d %H:%M")
        time_delta_sec = arrival - departure
        time_delta_min = round(time_delta_sec.total_seconds() / 60)
        return time_delta_min


@extend_schema(tags=["flights"])
class FlightFormAPIView(CreateAPIView, RetrieveAPIView):
    serializer_class = FlightFormSerializer
    queryset = Flight.objects.active()
    http_method_names = ("get", "post")

    @action(methods=["GET"], detail=False)
    def get(self, request, **kwargs):
        meta = self.metadata_class()
        data = meta.determine_metadata(request, self)
        form_schema = copy.deepcopy(data["actions"]["POST"])
        choice_fields = {
            "departure_airport": Airport.get_choices_dict(),
            "arrival_airport": Airport.get_choices_dict(),
            "aircraft": Aircraft.get_choices_dict(),
        }
        for name, choices in choice_fields.items():
            form_schema[name]["type"] = "choice"
            form_schema[name]["choices"] = choices
        return Response(form_schema)
