import pytest
from model_bakery import baker


__all__ = ["airport"]


@pytest.fixture()
def airport(db):
    def _airport(**kwargs):
        return baker.make("airports.Airport", **kwargs)

    return _airport
