from .models import Opinion
from django import forms


class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ('your_opinion',)
