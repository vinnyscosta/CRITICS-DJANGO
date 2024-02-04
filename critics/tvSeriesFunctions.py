import requests
from django.conf import settings

def discoverTvSeries():
    url_moviedb = f"{settings.URL_THE_MOVIE_DB}trending/tv/week?language=pt-BR"
    print(url_moviedb)
    response = requests.get(url_moviedb, headers=settings.HEADERS_THE_MOVIE_DB)
    data_moviedb = response.json().get('results', []) if response.status_code == 200 else []

    return data_moviedb

def moreTvSeries(movieId):
    url_moviedb = f"{settings.URL_THE_MOVIE_DB}tv/{movieId}?language=pt-BR"
    print(url_moviedb)
    response = requests.get(url_moviedb, headers=settings.HEADERS_THE_MOVIE_DB)
    data_moviedb = response.json() if response.status_code == 200 else {}

    return data_moviedb

def castTvSeries(movieId):
    url_moviedb = f"{settings.URL_THE_MOVIE_DB}tv/{movieId}/credits?language=pt-BR"
    response = requests.get(url_moviedb, headers=settings.HEADERS_THE_MOVIE_DB)
    data_moviedb = response.json().get('cast', []) if response.status_code == 200 else {}

    return data_moviedb

def providersTvSeries(movieId):
    url_moviedb = f"https://api.themoviedb.org/3/tv/{movieId}/watch/providers?language=pt-BR"
    headers = {'Authorization': f"Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZWJkNzQ0YWZlNDMxYWQzNDgzNGIyZTA4MzU2MjU3NiIsInN1YiI6IjY0ZTc2ZWJiZTg5NGE2MDExZWY3OWM3MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.pdlP35v1dN_DhwnFsrG7vfc3kxO970goxYQ8pUMQ9IQ"}
    response = requests.get(url_moviedb, headers=headers)
    data_moviedb = response.json().get('results', {}) if response.status_code == 200 else {}
    data_moviedb = data_moviedb.get('BR', {})

    return data_moviedb