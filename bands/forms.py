from .models import Opinion
from django import forms


class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ('please_rate_the_band', 'would_you_see_this_band_again', 'your_opinion',)
