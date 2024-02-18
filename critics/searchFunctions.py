import requests
from django.conf import settings

def searchMovieDb(searchText, page=1):
    url_moviedb = f"{settings.URL_THE_MOVIE_DB}search/multi?query={searchText}&language=pt-BR&page={page}"
    response = requests.get(url_moviedb, headers=settings.HEADERS_THE_MOVIE_DB)
    data_moviedb = response.json() if response.status_code == 200 else {}

    return data_moviedb