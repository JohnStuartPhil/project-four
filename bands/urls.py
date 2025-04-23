from . import views
from django.urls import path

urlpatterns = [
    path('', views.BandList.as_view(), name='home'),
]