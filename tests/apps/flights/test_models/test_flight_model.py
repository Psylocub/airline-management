import pytest

from aircraft_manager.apps.flights.models import Flight

pytestmark = pytest.mark.django_db


def test_queryset_active(flight):
    assert Flight.objects.count() == 0
    active_flight = flight(is_active=True)
    flight(is_active=False)
    flight(is_active=False)
    assert Flight.objects.count() == 3
    assert Flight.objects.active().count() == 1
    assert Flight.objects.active().first() == active_flight


def test_queryset_inactive(flight):
    assert Flight.objects.count() == 0
    inactive_flight = flight(is_active=False)
    flight(is_active=True)
    flight(is_active=True)
    assert Flight.objects.count() == 3
    assert Flight.objects.inactive().count() == 1
    assert Flight.objects.inactive().first() == inactive_flight
