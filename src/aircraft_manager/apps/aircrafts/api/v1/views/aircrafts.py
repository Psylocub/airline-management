from django_filters.rest_framework.backends import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView

from aircraft_manager.apps.aircrafts.api.v1.filters import AircraftFilterSet
from aircraft_manager.apps.aircrafts.api.v1.serializers import AircraftListSerializers
from aircraft_manager.apps.aircrafts.models import Aircraft


@extend_schema(tags=["aircrafts"])
class AircraftListAPIView(ListAPIView):
    serializer_class = AircraftListSerializers
    queryset = Aircraft.objects.all()
    filterset_class = AircraftFilterSet
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    ordering_fields = (
        "serial_number",
        "manufacturer",
    )
