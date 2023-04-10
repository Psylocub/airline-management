import pytest
from model_bakery import baker


__all__ = ["aircraft"]


@pytest.fixture()
def aircraft(db):
    def _aircraft(**kwargs):
        return baker.make("aircrafts.Aircraft", **kwargs)

    return _aircraft
