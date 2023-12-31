# Generated by Django 4.2.4 on 2023-08-19 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0003_name_actors_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='name',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='name',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='name',
            name='actors_name',
            field=models.CharField(default='ABC', max_length=255),
        ),
        migrations.AlterField(
            model_name='name',
            name='synopsis',
            field=models.TextField(default='Yamete Kudasai'),
        ),
    ]
