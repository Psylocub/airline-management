from django_filters.rest_framework.backends import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView

from aircraft_manager.apps.airports.api.v1.filters import AirportFilterSet
from aircraft_manager.apps.airports.api.v1.serializers import AirportListSerializers
from aircraft_manager.apps.airports.models import Airport


@extend_schema(tags=["airports"])
class AirportListAPIView(ListAPIView):
    serializer_class = AirportListSerializers
    queryset = Airport.objects.all()
    filterset_class = AirportFilterSet
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    ordering_fields = (
        "icao_code",
        "country",
    )
