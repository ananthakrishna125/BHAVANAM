from django.contrib import admin
from .models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "district",
    )

    list_filter = ("district",)

    search_fields = (
        "name",
        "district__name",
    )