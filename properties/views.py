from django.shortcuts import render, get_object_or_404
from .models import Property

def search_properties(request):

    properties = Property.objects.filter(status="AVAILABLE")

    district = request.GET.get("district")
    location = request.GET.get("location")
    purpose = request.GET.get("purpose")
    property_type = request.GET.get("property_type")

    if district:
        properties = properties.filter(district_id=district)

    if location:
        properties = properties.filter(location_id=location)

    if purpose:
        properties = properties.filter(purpose=purpose)

    if property_type:
        properties = properties.filter(property_type=property_type)

    context = {
        "properties": properties,
    }

    return render(request, "properties/search.html", context)





def property_detail(request, id):

    property = get_object_or_404(
        Property,
        id=id
    )

    similar_properties = Property.objects.filter(
        district=property.district,
        status="AVAILABLE"
    ).exclude(id=id)[:4]

    context = {
        "property": property,
        "similar_properties": similar_properties,
    }

    return render(
        request,
        "properties/detail.html",
        context
    )