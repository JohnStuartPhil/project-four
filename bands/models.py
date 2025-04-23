from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

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
