from django.urls import path
from . import views

urlpatterns = [
    path("get-locations/", views.get_locations, name="get_locations"),
]