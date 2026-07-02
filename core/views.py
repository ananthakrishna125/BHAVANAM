from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from districts.models import District
from django.shortcuts import redirect
from enquiries.models import Enquiry
from django.contrib.auth.models import User
from django.http import HttpResponse

def home(request):

    districts = District.objects.all()

    context = {
        "districts": districts
    }

    return render(request, "core/home.html", context)





def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Save enquiry
        Enquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,
        )

        # Try to send email
        try:
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
                fail_silently=True,
            )
        except Exception:
            pass

    return redirect("home")



def create_admin(request):
    username = "BHAVANAM"
    password = "ananthan2005KS"  # Change this
    email = "bhavanamforyou@gmail.com"         # Change this

    user, created = User.objects.get_or_create(
        username=username,
        defaults={"email": email}
    )

    user.email = email
    user.is_staff = True
    user.is_superuser = True
    user.set_password(password)
    user.save()

    if created:
        return HttpResponse("Admin user created successfully.")
    return HttpResponse("Admin password updated successfully.")