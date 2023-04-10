from django.contrib import admin

from aircraft_manager.apps.flights.models import Flight


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        "departure_airport",
        "arrival_airport",
        "departure_date",
        "arrival_date",
        "aircraft",
    )
    readonly_fields = ("created", "updated")
    fieldsets = (
        (None, {"fields": ("created", "updated", "is_active")}),
        ("Aircraft information", {"fields": ("aircraft",)}),
        ("Departure information", {"fields": ("departure_airport", "departure_date")}),
        ("Arrival information", {"fields": ("arrival_airport", "arrival_date")}),
    )
    autocomplete_fields = ("aircraft", "departure_airport", "arrival_airport")
