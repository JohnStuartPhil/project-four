from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_band_house(request):
    """
    Renders the Intro page
    """

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Thank your for your request to play at '
                                 'BAND HOUSE. We shall aim to respond to your '
                                 'request within 5 working days.')

    intro = About.objects.all().order_by('-venue_name').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "intro/intro.html",
        {
            "intro": intro,
            "collaborate_form": collaborate_form
        },
    )
