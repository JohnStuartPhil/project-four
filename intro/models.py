from django.db import models

# Create your models here.


class About(models.Model):
    venue_name = models.CharField(max_length=50)
    updated_on = models.DateTimeField(auto_now=True)
    about_us = models.TextField()

    def __str__(self):
        return self.venue_name
