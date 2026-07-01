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




def contact(request):
    if request.method == "POST":

        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        # Save enquiry
        Enquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,
        )

        # Send email to BHAVANAM
        send_mail(
            subject=f"New Enquiry from {name}",
            message=f"""
Name: {name}

Email: {email}

Phone: {phone}

Message:
{message}
""",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["bhavanamforyou@gmail.com"],
            fail_silently=False,
        )

        return redirect("home")

    return redirect("home")