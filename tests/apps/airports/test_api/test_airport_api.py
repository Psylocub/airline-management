import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_airport_list_api_get_success(api_client, airport):
    airport(is_active=True)
    client = api_client()
    response = client.get(reverse("api-v1-airports:list"))
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["count"] == 1
    keys = [
        "id",
        "icao_code",
        "country",
    ]
    assert all(key in response.json()["results"][0].keys() for key in keys)
