from __future__ import unicode_literals
from django.db import migrations

import json

def create_initial_products(apps, schema_editor):
    Movies = apps.get_model('movie_info', 'Movies')

    data = json.load(open("movie_info/migrations/imdb.json"))

    for movie in data:
        movie_model = Movies.objects.create(popularity = movie['99popularity'],
        director = movie['director'],
        genre = movie['genre'],
        imdb_score = movie['imdb_score'],
        name = movie['name'])
        movie_model.save()


class Migration(migrations.Migration):

    dependencies = [
        ('movie_info', '0004_merge_20180521_1652'),
    ]

    operations = [
        migrations.RunPython(create_initial_products),
    ]
