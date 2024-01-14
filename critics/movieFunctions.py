import requests
from django.conf import settings

def discover():
    url_moviedb = f"{settings.URL_THE_MOVIE_DB}discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
    response = requests.get(url_moviedb, headers=settings.HEADERS_THE_MOVIE_DB)
    data_moviedb = response.json().get('results', []) if response.status_code == 200 else []

    return data_moviedb

def movieMore(movieId):
    url_moviedb = f"{settings.URL_THE_MOVIE_DB}movie/{movieId}&language=pt-BR"
    response = requests.get(url_moviedb, headers=settings.HEADERS_THE_MOVIE_DB)
    data_moviedb = response.json() if response.status_code == 200 else {}

    return data_moviedb

def castMovie(movieId):
    url_moviedb = f"{settings.URL_THE_MOVIE_DB}movie/{movieId}/credits?language=en-US"
    response = requests.get(url_moviedb, headers=settings.HEADERS_THE_MOVIE_DB)
    data_moviedb = response.json().get('cast', []) if response.status_code == 200 else {}

    return data_moviedb