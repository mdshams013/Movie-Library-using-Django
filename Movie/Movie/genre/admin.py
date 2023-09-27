from django.contrib import admin

from .models import Genre, Name

from dashboard.models import List,ListItems

admin.site.register(Genre)
admin.site.register(Name)
admin.site.register(List)
admin.site.register(ListItems)