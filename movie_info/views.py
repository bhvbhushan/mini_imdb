from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies


def home(request):
    movies = Movies.objects.all()
    return render(request, 'home.html', {'movies': movies})
