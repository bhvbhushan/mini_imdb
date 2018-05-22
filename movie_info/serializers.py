from .models import Movies, MovieReview
from rest_framework import serializers

class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = ('id', 'name', 'popularity', 'director', 'imdb_score',  'genre')


class ReviewSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = MovieReview
        fields = ('id', 'title', 'review', 'rating', 'created_by')
