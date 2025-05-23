from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Band, Opinion
from .forms import OpinionForm

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

    if request.method == "POST":
        opinion_form = OpinionForm(data=request.POST)
        if opinion_form.is_valid():
            opinion = opinion_form.save(commit=False)
            opinion.author = request.user
            opinion.band = band
            opinion.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you for providing your Opinion. This is '
                'currently awaiting authorisation to be published'
            )

    opinion_form = OpinionForm()

    return render(
        request,
        "bands/band_detail.html",
        {
            "band": band,
            "opinions": opinions,
            "opinion_count": opinion_count,
            "opinion_form": opinion_form,
        },
    )


def opinion_edit(request, slug, opinion_id):
    """
    view to edit opinions
    """
    if request.method == "POST":

        queryset = Band.objects.filter(status=1)
        band = get_object_or_404(queryset, slug=slug)
        opinion = get_object_or_404(Opinion, pk=opinion_id)
        opinion_form = OpinionForm(data=request.POST, instance=opinion)

        if opinion_form.is_valid() and opinion.author == request.user:
            opinion = opinion_form.save(commit=False)
            opinion.band = band
            opinion.approved = False
            opinion.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Thank you for updating your opinion. '
                                 'This is currently awaiting '
                                 'authorisation to be published.')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating opinion!')

    return HttpResponseRedirect(reverse('band_detail', args=[slug]))


def opinion_delete(request, slug, opinion_id):
    """
    view to delete opinion
    """
    queryset = Band.objects.filter(status=1)
    band = get_object_or_404(queryset, slug=slug)
    opinion = get_object_or_404(Opinion, pk=opinion_id)

    if opinion.author == request.user:
        opinion.delete()
        opinion.band = band
        messages.add_message(request, messages.SUCCESS, 'Your opinion has '
                             'been deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own opinions!')

    return HttpResponseRedirect(reverse('band_detail', args=[slug]))
