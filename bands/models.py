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

RATING_CHOICES = (
    ('Please Select', 'Please Select'),
    ('very bad', 'very bad'),
    ('bad', 'bad'),
    ('average', 'average'),
    ('good', 'good'),
    ('very good', 'very good')
    )

AGAIN_CHOICES = (
    ('Please Select', 'Please Select'),
    ('yes', 'yes'),
    ('no', 'no'),
    ('maybe', 'maybe')
    )
# Create your models here.


class Band(models.Model):
    band_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    genre = models.CharField(choices=GENRE_CHOICES, default='Please select',
                             unique=False)
    number_of_members = models.CharField(
        choices=MEMBER_CHOICES, default='Please select', unique=False
    )
    review = models.TextField()
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
    band_name = models.ForeignKey(
        Band, on_delete=models.CASCADE, related_name="opinions")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="opinionator")
    rating = models.CharField(choices=RATING_CHOICES, default='Please select',
                             unique=False)
    again = models.CharField(choices=AGAIN_CHOICES, default='Please select',
                             unique=False)
    your_opinion = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Opinion given by {self.author}: {self.your_opinion}"
