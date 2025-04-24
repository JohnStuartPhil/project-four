from django.shortcuts import render
from django.views import generic
from .models import Band

# Create your views here.


# class BandList(generic.ListView):
    # model = Band

class BandList(generic.ListView):
    queryset = Band.objects.filter(status=1)
    # template_name = "band_list.html"
    template_name = "bands/index.html"
    paginate_by = 6
