from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Genres'
    
    def __str__(self):
        return self.name

class Name(models.Model):
    genre = models.ForeignKey(Genre, related_name='genre', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    synopsis = models.TextField(blank=False, null=False, default='Write synopsis')
    director_name = models.CharField(max_length=255)
    actors_name = models.CharField(max_length=255, blank=False, null=False, default='ABC')
    year = models.IntegerField(default=0000)
    image = models.ImageField(upload_to='genre_images')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name



