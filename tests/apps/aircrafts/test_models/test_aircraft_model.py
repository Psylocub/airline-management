import pytest

from aircraft_manager.apps.aircrafts.models import Aircraft

pytestmark = pytest.mark.django_db


def test_queryset_active(aircraft):
    assert Aircraft.objects.count() == 0
    active_aircraft = aircraft(is_active=True)
    aircraft(is_active=False)
    aircraft(is_active=False)
    assert Aircraft.objects.count() == 3
    assert Aircraft.objects.active().count() == 1
    assert Aircraft.objects.active().first() == active_aircraft


def test_queryset_inactive(aircraft):
    assert Aircraft.objects.count() == 0
    inactive_aircraft = aircraft(is_active=False)
    aircraft(is_active=True)
    aircraft(is_active=True)
    assert Aircraft.objects.count() == 3
    assert Aircraft.objects.inactive().count() == 1
    assert Aircraft.objects.inactive().first() == inactive_aircraft
