import pytest
from rest_framework.test import APIClient

__all__ = ["api_client", "unauthorized_api_client"]


@pytest.fixture()
def unauthorized_api_client():
    return APIClient()


@pytest.fixture()
def api_client(user_account):
    def _api_client(auth_user=None):
        if auth_user is None:
            auth_user = user_account()
        client = APIClient()
        client.force_authenticate(auth_user)
        return client

    return _api_client
