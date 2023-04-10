from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from aircraft_manager import get_version

admin.site.site_header = f"Flight-manager admin {get_version()}"
admin.site.index_title = "Management area"
admin.site.site_title = "Flight-manager admin"

API_PREFIX = "api"

admin_urlpatterns = [
    path("admin/", admin.site.urls),
]

api_v1_urlpatterns = [
    path(
        f"{API_PREFIX}/v1/flights/",
        include(
            ("aircraft_manager.apps.flights.api.v1.urls", "flights"),
            namespace="api-v1-flights",
        ),
    ),
    path(
        f"{API_PREFIX}/v1/aircrafts/",
        include(
            ("aircraft_manager.apps.aircrafts.api.v1.urls", "aircrafts"),
            namespace="api-v1-aircrafts",
        ),
    ),
    path(
        f"{API_PREFIX}/v1/airports/",
        include(
            ("aircraft_manager.apps.airports.api.v1.urls", "airports"),
            namespace="api-v1-airports",
        ),
    ),
]

urlpatterns = admin_urlpatterns + api_v1_urlpatterns
swagger_urlpatterns = [
    path("api/schema/swagger.json", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="schema-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns += swagger_urlpatterns

# Enable serve static by django for local develop
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
