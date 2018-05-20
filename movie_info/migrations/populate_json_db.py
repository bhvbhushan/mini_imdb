from __future__ import unicode_literals
from django.db import migrations

import json


def create_initial_products(apps, schema_editor):
    GenreTypes = apps.get_model('movie_info', 'GenreTypes')

    data = json.load(open("movie_info/migrations/imdb.json"))

    genre_list = []
    for movie in data:
        for genre in list(set(movie["genre"])):
            genre_list.append(genre)

    for each_genre in list(set(genre_list)):
        genre_model = GenreTypes(genre_type=each_genre)
        genre_model.save()


class Migration(migrations.Migration):

    dependencies = [
        ('movie_info', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_products),
    ]
