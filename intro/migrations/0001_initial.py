# Generated by Django 4.2.20 on 2025-04-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=50)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('about_us', models.TextField()),
            ],
        ),
    ]
