# Generated by Django 4.2.20 on 2025-05-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0008_rename_rating_opinion_please_rate_the_band_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='number_of_members',
            field=models.CharField(choices=[('Please Select', 'Please Select'), ('Solo artist', 'Solo artist'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7 or more', '7 or more')], default='Please select'),
        ),
    ]
