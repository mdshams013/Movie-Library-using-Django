from django.db import models
from django.contrib.auth.models import User
from genre.models import Name, Genre

class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lists')

class ListItems(models.Model):
    mlist = models.ForeignKey(List, on_delete=models.CASCADE, related_name='list_items')
    movie = models.ForeignKey(Name, on_delete=models.SET_NULL, null=True , blank=True)
