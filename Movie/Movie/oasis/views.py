from django.shortcuts import render, redirect
from genre.models import Genre, Name

from .forms import SignupForm

def index(request):
    genres = Genre.objects.all()
    names = Name.objects.all()
    return render(request, 'oasis/index.html', {
        'genres' : genres,
        'names' : names,
    })

def add(request):
    return render(request, 'oasis/add.html')

def movie(request):
    return render(request, 'oasis/movie.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
        
    else:
        form = SignupForm()

    return render(request, 'oasis/signup.html',{
        'form': form
    })