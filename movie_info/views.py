from django.shortcuts import render, redirect
from django.http import Http404
from .models import Movies, MovieReview
from django.contrib.auth.models import User

from rest_framework import generics
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import MoviesSerializer, ReviewSerializer
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

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    permission_classes = (IsAdminOrReadOnly, )
    lookup_url_kwarg = 'movies_id'

class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    lookup_url_kwarg = 'movies_id'

    def perform_create(self, serializer):
        # We automatically set the user using the one who is logged in
        serializer.save(
            created_by=self.request.user,
            movies_id=self.kwargs['movies_id'])

    def get_queryset(self):
        movie = self.kwargs['movies_id']
        return MovieReview.objects.filter(movie__id=movie)


# Return a single Review (even for anonymous users) and allows user
# who created it to update and delete a single Review.
#
# GET    movies/<movies_id>/reviews/<review_id>/: return a Review
# PUT    movies/<movies_id>/reviews/<review_id>/: update a Review
# PATCH  movies/<movies_id>/reviews/<review_id>/: patch a Review
# DELETE movies/<movies_id>/reviews/<review_id>/: delete a Review
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    lookup_url_kwarg = 'review_id'

    def get_queryset(self):
        review = self.kwargs['review_id']
        return MovieReview.objects.filter(id=review)

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
