from django.contrib import admin

from aircraft_manager.apps.airports.models import Airport


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ("icao_code", "country", "updated", "is_active")
    readonly_fields = ("created", "updated")
    fieldsets = (
        (None, {"fields": ("created", "updated", "is_active")}),
        ("Basic information", {"fields": ("icao_code", "country")}),
    )
    search_fields = ("icao_code",)
