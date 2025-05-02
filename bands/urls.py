from . import views
from django.urls import path

urlpatterns = [
    path('', views.BandList.as_view(), name='home'),
    path('<slug:slug>/', views.band_detail, name='band_detail'),
    path('<slug:slug>/edit_opinion/<int:opinion_id>',
         views.opinion_edit, name='opinion_edit'),
]
