import pytest

from aircraft_manager.apps.airports.models import Airport

pytestmark = pytest.mark.django_db


def test_queryset_active(airport):
    assert Airport.objects.count() == 0
    active_airport = airport(is_active=True)
    airport(is_active=False)
    airport(is_active=False)
    assert Airport.objects.count() == 3
    assert Airport.objects.active().count() == 1
    assert Airport.objects.active().first() == active_airport


def test_queryset_inactive(airport):
    assert Airport.objects.count() == 0
    inactive_airport = airport(is_active=False)
    airport(is_active=True)
    airport(is_active=True)
    assert Airport.objects.count() == 3
    assert Airport.objects.inactive().count() == 1
    assert Airport.objects.inactive().first() == inactive_airport
