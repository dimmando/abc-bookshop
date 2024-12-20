from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

from django.contrib import messages
from django.http import HttpResponse


def contact(request):
    """
    Sending request to ABC Bookshop owners
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email_address"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())

            try:
                send_mail(
                    subject,
                    message,
                    "dimmando.travel@gmail.com",
                    ["dimmando.travel@gmail.com"],
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            messages.success(request, "Your inquiry was sent successfully.")
            return redirect("thanks")
        else:
            messages.warning(
                request, "Wrong email. It should look like name@domain.com."
            )
    else:
        form = ContactForm()

    context = {
        "form": form,
        "on_page": True,
    }

    return render(request, "contact/contact.html", context)


def thanks(request):
    """A view to return the thank you page"""

    return render(request, "contact/thankyou.html")
