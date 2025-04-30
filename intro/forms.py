from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('your_band_name', 'your_name', 'genre',
                  'number_of_members', 'email', 'tell_us_about_your_band')
