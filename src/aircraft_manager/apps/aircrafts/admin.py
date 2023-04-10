from django.contrib import admin

from aircraft_manager.apps.aircrafts.models import Aircraft


@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ("serial_number", "manufacturer", "updated", "is_active")
    readonly_fields = ("created", "updated")
    fieldsets = (
        (None, {"fields": ("created", "updated", "is_active")}),
        ("Basic information", {"fields": ("serial_number", "manufacturer")}),
    )
    search_fields = ("serial_number",)
