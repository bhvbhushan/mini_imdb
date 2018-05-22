"""mini_imdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token

# from accounts import views as accounts_views
from movie_info import views

urlpatterns = [
    url(r'^docs/', include_docs_urls(title='Mini IMDb API', public=True)),
    url(r'^$', views.home, name='home'),
    url(r'(?P<pk>\d+)/$', views.movie_info, name='movie_info'),
    url(r'^api-token-auth/', obtain_auth_token),
    # url(r'^signup/$', accounts_views.signup, name='signup'),
    # url(r'^(?P<pk>\d+)/new/$', views.new_review, name='new_review'),
    url(r'^admin/', admin.site.urls),

]
