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
