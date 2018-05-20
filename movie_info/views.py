from django.shortcuts import render
from .models import Movies


def home(request):
    movies = Movies.objects.all()
    query = request.GET.get("q")
    if query:
        movies = (movies.filter(name__icontains=query)) |\
        (movies.filter(director__icontains=query)) |\
        (movies.filter(genre__icontains=query))
    return render(request, 'home.html', {'movies': movies})


def movie_info(request, pk):
    movie = Movies.objects.get(pk=pk)
    return render(request, 'movie_info.html', {'movie': movie})
