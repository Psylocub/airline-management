import datetime
import json
import os

import pytest
from model_bakery import baker

__all__ = ["flight", "flight_schema", "flight_create_data"]


@pytest.fixture()
def flight(db):
    def _flight(**kwargs):
        return baker.make("flights.Flight", **kwargs)

    return _flight


@pytest.fixture()
def flight_schema():
    file_location = os.path.dirname(__file__) + "/resources/flight_form.json"
    with open(file_location) as f:
        yield json.load(f)


@pytest.fixture()
def flight_create_data():
    return {
        "departure_airport": None,
        "departure_date": (
            datetime.datetime.now() + datetime.timedelta(days=1)
        ).isoformat(),
        "arrival_airport": None,
        "arrival_date": (
            datetime.datetime.now() + datetime.timedelta(days=2)
        ).isoformat(),
        "aircraft": None,
    }
