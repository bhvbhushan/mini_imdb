from django.db import models
from django.contrib.auth.models import User


class Movies(models.Model):
    popularity = models.FloatField()
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default='Not Available')
    imdb_score = models.FloatField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MovieReview(models.Model):
    title = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.cascade)
