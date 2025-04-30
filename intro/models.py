from django.db import models

# Create your models here.


class About(models.Model):
    venue_name = models.CharField(max_length=50)
    updated_on = models.DateTimeField(auto_now=True)
    about_us = models.TextField()

    def __str__(self):
        return self.venue_name


class CollaborateRequest(models.Model):
    your_band_name = models.CharField(max_length=50)
    email = models.EmailField()
    tell_us_about_your_band = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.your_band_name}"
