from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewMovie
from .models import Name

def detail(request, pk):
    name = get_object_or_404(Name, pk=pk)

    return render(request, 'genre/detail.html',{
        'name' : name
    })

@login_required
def new(request):
    if request.method == 'POST':
        add = NewMovie(request.POST, request.FILES)

        if add.is_valid():
            name = add.save(commit=False)
            name.save()

            return redirect('genre:detail',pk=name.id)
    else:   
        add = NewMovie()

    return render(request, 'genre/add.html',{
        'add' : add
    })

