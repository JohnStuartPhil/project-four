# Generated by Django 4.2.20 on 2025-05-02 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0007_rename_band_name_opinion_band'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opinion',
            old_name='rating',
            new_name='please_rate_the_band',
        ),
        migrations.RenameField(
            model_name='opinion',
            old_name='again',
            new_name='would_you_see_this_band_again',
        ),
    ]
