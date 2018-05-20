from django.test import TestCase
from django.urls import reverse, resolve
from .views import home, movie_info
from .models import Movies

# Create your tests here.
class HomeTests(TestCase):
    def setUp(self):
        self.Movie = Movies.objects.create(name='Test Movie', director = 'Test Director',
        imdb_score = 7.8, popularity = 78, genre = 'Testing')
        url = reverse(home)
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_movie_info_view_contains_link_back_to_homepage(self):
        movie_info_url = reverse('movie_info', kwargs={'pk': 1})
        response = self.client.get(movie_info_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))

class MovieInfoTests(TestCase):
    def setUp(self):
        Movies.objects.create(name='Test Movie', director = 'Test Director',
        imdb_score = 7.8, popularity = 78, genre = 'Testing')

    def test_movie_info_view_success_status_code(self):
        url = reverse('movie_info', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_movie_info_view_not_found_status_code(self):
        url = reverse('movie_info', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_movie_info_url_resolves_movie_info_view(self):
        view = resolve('/1/')
        self.assertEquals(view.func, movie_info)
