# Generated by Django 4.2.20 on 2025-04-29 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0006_alter_band_options_alter_opinion_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opinion',
            old_name='band_name',
            new_name='band',
        ),
    ]
