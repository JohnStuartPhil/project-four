from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Published")
    )

GENRE_CHOICES = (
    ('Please Select', 'Please Select'),
    ('Pop', 'Pop'),
    ('Rock', 'Rock'),
    ('Metal', 'Metal'),
    ('Punk', 'Punk'),
    ('Blues', 'Blues'),
    ('Jazz', 'Jazz'),
    ('Fusion', 'Fusion')
    )

MEMBER_CHOICES = (
    ('Please Select', 'Please Select'),
    ('Solo artist', 'Solo artist'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7 or more', '7 or more')
    )

RATING_CHOICES = (
    ('', ''),
    ('very bad', 'very bad'),
    ('bad', 'bad'),
    ('average', 'average'),
    ('good', 'good'),
    ('very good', 'very good')
    )

AGAIN_CHOICES = (
    ('', ''),
    ('yes', 'yes'),
    ('no', 'no'),
    ('maybe', 'maybe')
    )


class Band(models.Model):
    band_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    genre = models.CharField(choices=GENRE_CHOICES, default='Please select',
                             unique=False)
    number_of_members = models.CharField(
        choices=MEMBER_CHOICES, default='Please select', unique=False
    )
    review = models.TextField(max_length=500)
    review_excerpt = models.TextField(blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="band_posts"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.band_name} reviewed by {self.author}"


class Opinion(models.Model):
    band = models.ForeignKey(
        Band, on_delete=models.CASCADE, related_name="opinions")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="opinionator")
    would_you_see_this_band_again = models.CharField(
        choices=AGAIN_CHOICES, default='', unique=False)
    please_rate_the_band = models.CharField(
        choices=RATING_CHOICES, default='', unique=False)
    your_opinion = models.TextField(max_length=250)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Opinion given by {self.author}: {self.your_opinion}"
