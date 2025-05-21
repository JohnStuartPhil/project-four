from django.db import models

# Create your models here.


class About(models.Model):
    venue_name = models.CharField(max_length=50)

    def __str__(self):
        return self.venue_name


class CollaborateRequest(models.Model):
    your_band_name = models.CharField(max_length=50)
    your_name = models.CharField(max_length=50)
    email = models.EmailField()
    tell_us_about_your_band = models.TextField(max_length=3000)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.your_band_name}"
