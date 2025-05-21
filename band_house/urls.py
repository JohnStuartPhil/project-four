"""
URL configuration for band_house project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.intro, name='intro')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Intro.as_view(), name='intro')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('bands/', include('bands.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("intro.urls"), name="intro-urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("bands/", include("bands.urls"), name="bands-urls"),
]
