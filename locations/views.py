from django.http import JsonResponse
from .models import Location

def get_locations(request):

    district_id = request.GET.get("district")

    locations = Location.objects.filter(
        district_id=district_id
    ).values("id", "name")

    return JsonResponse(list(locations), safe=False)
