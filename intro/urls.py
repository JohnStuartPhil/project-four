from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_band_house, name='intro'),
]
