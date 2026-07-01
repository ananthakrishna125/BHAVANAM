from django.urls import path
from . import views

urlpatterns = [
    path("search/", views.search_properties, name="search_properties"),
    path("<int:id>/", views.property_detail, name="property_detail"),
]