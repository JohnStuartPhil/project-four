from django.shortcuts import render
from .models import About
from .forms import CollaborateForm


def about_band_house(request):
    """
    Renders the Intro page
    """
    intro = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "intro/intro.html",
        {
            "intro": intro,
            "collaborate_form": collaborate_form
        },
    )

# Create your views here.
