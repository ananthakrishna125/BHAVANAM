from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("contact/", views.contact, name="contact"),
    

    # Temporary - remove after use
    path("create-admin/", views.create_admin, name="create_admin"),
]
]