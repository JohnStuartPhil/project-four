from django.shortcuts import render
from .models import About


def about_band_house(request):
    """
    Renders the Intro page
    """
    intro = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "intro/intro.html",
        {"intro": intro},
    )

# Create your views here.
