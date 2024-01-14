import requests
from django.shortcuts import render
from critics.movieFunctions import *

def index(request):

    data_moviedb = discover()

    return render(request, 'critics/index.html', {'movies': data_moviedb,})

def movie(request,movieId):
    
    data_moviedb = movieMore(movieId)
    cast_moviedb = castMovie(movieId)

    return render(request, 'critics/movie.html', {'movie': data_moviedb,'cast': cast_moviedb,})

def login(request):
    return render(request, 'critics/login.html')