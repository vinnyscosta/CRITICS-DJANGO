import requests
from django.conf import settings

def discoverMovie():
    url_moviedb = f"{settings.URL_THE_MOVIE_DB}discover/movie?language=pt-BR&page=1&sort_by=popularity.desc"
    response = requests.get(url_moviedb, headers=settings.HEADERS_THE_MOVIE_DB)
    data_moviedb = response.json().get('results', []) if response.status_code == 200 else []

    return data_moviedb

def moreMovie(movieId):
    url_moviedb = f"{settings.URL_THE_MOVIE_DB}movie/{movieId}?language=pt-BR"
    response = requests.get(url_moviedb, headers=settings.HEADERS_THE_MOVIE_DB)
    data_moviedb = response.json() if response.status_code == 200 else {}

    return data_moviedb

def castMovie(movieId):
    url_moviedb = f"{settings.URL_THE_MOVIE_DB}movie/{movieId}/credits?language=pt-BR"
    response = requests.get(url_moviedb, headers=settings.HEADERS_THE_MOVIE_DB)
    cast_moviedb = response.json().get('cast', []) if response.status_code == 200 else {}
    crew_moviedb = response.json().get('crew', []) if response.status_code == 200 else {}

    return cast_moviedb,crew_moviedb

def providersMovie(movieId):
    url_moviedb = f"{settings.URL_THE_MOVIE_DB}movie/{movieId}/watch/providers?language=pt-BR"
    headers = {'Authorization': f"Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZWJkNzQ0YWZlNDMxYWQzNDgzNGIyZTA4MzU2MjU3NiIsInN1YiI6IjY0ZTc2ZWJiZTg5NGE2MDExZWY3OWM3MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.pdlP35v1dN_DhwnFsrG7vfc3kxO970goxYQ8pUMQ9IQ"}
    response = requests.get(url_moviedb, headers=headers)
    data_moviedb = response.json().get('results', {}) if response.status_code == 200 else {}
    data_moviedb = data_moviedb.get('BR', {})

    return data_moviedb

def similarMovie(movieId):
    url_moviedb = f"{settings.URL_THE_MOVIE_DB}movie/{movieId}/similar?language=pt-BR&page=1"
    response = requests.get(url_moviedb, headers=settings.HEADERS_THE_MOVIE_DB)
    data_moviedb = response.json().get('results', []) if response.status_code == 200 else []

    return data_moviedb