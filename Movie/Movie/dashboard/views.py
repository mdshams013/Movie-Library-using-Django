from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from genre.models import Name
from .models import List,ListItems

def add_to_list(request, uid):
    movie = Name.objects.get(uid = uid)
    user = request.user
    mlist , _ = List.objects.get_or_create(user = user , is_paid = False)

    list_item = ListItems.objects.create(mlist = mlist, movie = movie)
    list_item.save()

    return HttpResponseRedirect(request.path_info)