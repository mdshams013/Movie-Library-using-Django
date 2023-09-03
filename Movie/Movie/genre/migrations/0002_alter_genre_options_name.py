# Generated by Django 4.2.4 on 2023-08-18 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('name',), 'verbose_name_plural': 'Genres'},
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('director_name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='genre_images')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='genre.genre')),
            ],
        ),
    ]
