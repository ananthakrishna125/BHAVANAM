from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from districts.models import District
from django.shortcuts import redirect
from enquiries.models import Enquiry


def home(request):

    districts = District.objects.all()

    context = {
        "districts": districts
    }

    return render(request, "core/home.html", context)









