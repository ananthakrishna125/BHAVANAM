from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from properties.models import Property
from districts.models import District
from locations.models import Location

@login_required
def dashboard(request):

    context = {
        "total_properties": Property.objects.count(),
        "available_properties": Property.objects.filter(status="AVAILABLE").count(),
        "districts": District.objects.count(),
        "locations": Location.objects.count(),
        "latest_properties": Property.objects.order_by("-id")[:5],
    }

    return render(request, "dashboard/dashboard.html", context)
