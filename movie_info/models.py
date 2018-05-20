from django.db import models
from django.contrib.auth.models import User


class GenreTypes(models.Model):
    genre_type = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_type


class Movies(models.Model):
    popularity = models.FloatField()
    director = models.CharField(max_length=100)
    genre = models.ManyToManyField(GenreTypes)
    imdb_score = models.FloatField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    movie = models.ForeignKey(Movies, related_name='reviews', on_delete=models.CASCADE,)
    title = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE,)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE,)
