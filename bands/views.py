from django.shortcuts import render
from django.views import generic
from .models import Band

# Create your views here.


class BandList(generic.ListView):
    model = Band