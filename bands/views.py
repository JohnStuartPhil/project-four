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
                'Opinion submitted and awaiting approval'
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


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Band.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Opinion, pk=comment_id)
        comment_form = OpinionForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('band_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Band.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Opinion, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('band_detail', args=[slug]))