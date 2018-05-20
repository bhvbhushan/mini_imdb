from django.shortcuts import render, redirect
from django.http import Http404
from .models import Movies
from django.contrib.auth.models import User


def home(request):
    movies = Movies.objects.all()
    query = request.GET.get("q")
    if query:
        movies = (movies.filter(name__icontains=query)) |\
        (movies.filter(director__icontains=query)) |\
        (movies.filter(genre__icontains=query))
    return render(request, 'home.html', {'movies': movies})


def movie_info(request, pk):
    try:
        movie = Movies.objects.get(pk=pk)
    except Movies.DoesNotExist:
        raise Http404
    return render(request, 'movie_info.html', {'movie': movie})
