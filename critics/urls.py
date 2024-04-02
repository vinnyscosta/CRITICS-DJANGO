from django.urls import path
from critics.views import *

urlpatterns = [
    path('', index, name='index'),
    path('cadastro', cadastro, name='cadastro'),
    path('my-profile', my_profile, name='my-profile'),
    path('trending', trending, name='trending'),
    path('search/<int:page>', search, name='search'),
    path('movie/<int:movieId>', movie, name='movie'),
    path('tvSeries/<int:tvSeriesId>', tvSeries, name='tvSeries'),
    path('tvSeries/<int:tvSeriesId>/season/<int:seasonNumber>', season, name='season'),
    path('tvSeries/<int:tvSeriesId>/season/<int:seasonNumber>/episode/<int:episodeNumber>', episode, name='episode'),
    path('person/<int:personId>', person, name='person'),
    path('logout', logout, name='logout'),
]