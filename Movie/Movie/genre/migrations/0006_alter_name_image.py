# Generated by Django 4.2.4 on 2023-08-19 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0005_alter_name_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='image',
            field=models.ImageField(upload_to='genre_images'),
        ),
    ]