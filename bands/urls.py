from . import views
from django.urls import path

urlpatterns = [
    path('', views.BandList.as_view(), name='home'),
    path('<slug:slug>/', views.band_detail, name='band_detail'),
]
