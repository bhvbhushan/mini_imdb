from django.shortcuts import render, redirect
from django.http import Http404
from .models import Movies
from django.contrib.auth.models import User

from rest_framework import generics
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import MoviesSerializer
from rest_framework import filters

from django.shortcuts import render
# Lists and Creates entries of Movies
#
# GET  products/: return a list of Products
# POST products/: create a Product
#      data = {
#      }
class MovieList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    permission_classes = (IsAdminOrReadOnly, )
    lookup_url_kwarg = 'movies_id'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

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

# def new_review(request, pk):
#     try:
#         movie = Movies.objects.get(pk=pk)
#     except Movies.DoesNotExist:
#         raise Http404
#     return render(request, 'new_review.html', {'movie': movie})
