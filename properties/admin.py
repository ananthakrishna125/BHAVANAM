from django.contrib import admin
from .models import Property, PropertyImage


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 5  # Show 5 empty image upload fields


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "district",
        "location",
        "price",
        "status",
    )

    search_fields = (
        "title",
        "district__name",
        "location__name",
    )

    list_filter = (
        "district",
        "purpose",
        "property_type",
        "status",
    )

    inlines = [PropertyImageInline]