from django.db import models

GENRE_CHOICES = (
    ('Please Select', 'Please Select'),
    ('Pop', 'Pop'),
    ('Rock', 'Rock'),
    ('Blues', 'Blues'),
    ('Jazz', 'Jazz'),
    ('Fusion', 'Fusion')
    )

MEMBER_CHOICES = (
    ('Please Select', 'Please Select'),
    ('Solo artist', 'Solo artist'),
    ('Two', 'Two'),
    ('Three', 'Three'),
    ('Four', 'Four'),
    ('Five', 'Five'),
    ('Six', 'Six'),
    ('Seven or more', 'Seven or more')
    )

# Create your models here.


class About(models.Model):
    venue_name = models.CharField(max_length=50)
    updated_on = models.DateTimeField(auto_now=True)
    about_us = models.TextField()

    def __str__(self):
        return self.venue_name


class CollaborateRequest(models.Model):
    your_band_name = models.CharField(max_length=50)
    your_name = models.CharField(max_length=50)
    genre = models.CharField(choices=GENRE_CHOICES, default='Please select',
                             unique=False)
    number_of_members = models.CharField(
        choices=MEMBER_CHOICES, default='Please select', unique=False
    )
    email = models.EmailField()
    tell_us_about_your_band = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.your_band_name}"
