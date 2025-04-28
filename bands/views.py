from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Band

# Create your views here.


class BandList(generic.ListView):
    queryset = Band.objects.filter(status=1)
    template_name = "bands/index.html"
    paginate_by = 6


def band_detail(request, slug):
    """
    Display an individual :model:`bands.Band`.

    **Context**

    ``bandpost``
        An instance of :model:`bands.Band`.

    **Template:**

    :template:`bands/band_detail.html`
    """

    queryset = Band.objects.filter(status=1)
    band = get_object_or_404(queryset, slug=slug)
    opinions = band.opinions.all().order_by("-created_on")
    opinion_count = band.opinions.filter(approved=True).count()

    return render(
        request,
        "bands/band_detail.html",
        {
            "band": band,
            "opinions": opinions,
            "opinion_count": opinion_count,
        },
    )
