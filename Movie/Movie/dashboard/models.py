from django.db import models
from django.contrib.auth.models import User
from genre.models import Name

class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='lists')

class ListItems(models.Model):
    list1 = models.ForeignKey(List, on_delete=models.CASCADE, related_name='list_items')
    name = models.ForeignKey(Name, on_delete=models.SET_NULL, null=True ,blank=True)

    class Meta:
        ordering = ('name',)

