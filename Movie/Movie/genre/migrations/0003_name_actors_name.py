# Generated by Django 4.2.4 on 2023-08-19 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0002_alter_genre_options_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='actors_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
