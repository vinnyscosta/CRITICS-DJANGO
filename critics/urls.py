from django.urls import path
from critics.views import index, search, movie, tvSeries, person, logout, cadastro

urlpatterns = [
    path('', index, name='index'),
    path('cadastro', cadastro, name='cadastro'),
    path('search/<int:page>', search, name='search'),
    path('movie/<int:movieId>', movie, name='movie'),
    path('tvSeries/<int:tvSeriesId>', tvSeries, name='tvSeries'),
    path('person/<int:personId>', person, name='person'),
    path('logout', logout, name='logout'),
]