import pytest
from model_bakery import baker


__all__ = ["user_account"]


@pytest.fixture()
def user_account(db):
    def _user_account(**kwargs):
        return baker.make("auth.User", **kwargs)

    return _user_account
