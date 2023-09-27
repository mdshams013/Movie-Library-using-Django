from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from dashboard.models import List, ListItems
from genre.models import Name

@login_required
def add_to_list(request, pk):
    
    name = get_object_or_404(Name, pk=pk)
    user = request.user
    list1 , _ = List.objects.get_or_create(user = user)
    list_item = ListItems.objects.create(list1 = list1 , name = name , )
    list_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def list(request):
    lists = List.objects.filter(user=request.user)
    items = ListItems.objects.filter(list1=lists[0])
    context = {'items': items}
    #context = {'list' : List.objects.filter(user = request.user)}
    return render(request, 'dashboard/list.html', context)