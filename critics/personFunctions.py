import requests
from django.conf import settings

def morePerson(personId):
    url_moviedb = f"{settings.URL_THE_MOVIE_DB}person/{personId}?language=pt-BR"
    print(url_moviedb)
    response = requests.get(url_moviedb, headers=settings.HEADERS_THE_MOVIE_DB)
    data_moviedb = response.json() if response.status_code == 200 else {}

    return data_moviedb

def movieCreditsPerson(personId):
    url_moviedb = f"{settings.URL_THE_MOVIE_DB}person/{personId}/movie_credits?language=pt-BR"
    response = requests.get(url_moviedb, headers=settings.HEADERS_THE_MOVIE_DB)
    data_moviedb = response.json() if response.status_code == 200 else {}

    return data_moviedb

def TvCreditsPerson(personId):
    url_moviedb = f"{settings.URL_THE_MOVIE_DB}person/{personId}/tv_credits?language=pt-BR"
    print(url_moviedb)
    response = requests.get(url_moviedb, headers=settings.HEADERS_THE_MOVIE_DB)
    data_moviedb = response.json() if response.status_code == 200 else {}

    return data_moviedb