import requests
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from critics.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User
from critics.searchFunctions import *
from critics.movieFunctions import *
from critics.tvSeriesFunctions import *
from critics.seasonFunctions import *
from critics.personFunctions import *

def index(request):
    print(request.user)

    people_moviedb = discoverPeople()
    movies_moviedb = discoverMovie()
    tvSeries_moviedb = discoverTvSeries()

    formLog = LoginForms()

    if request.method == 'POST':
        formLog = LoginForms(request.POST)

        if formLog.is_valid():
            nome=formLog['nome_login'].value()
            senha=formLog['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"{nome} logado com sucesso!")
            return redirect('index')
        
        else:
            messages.error(request, f"Erro ao efetuar login!")
            return redirect('index')

    return render(request, 'critics/index.html', 
                  {
                    'people':people_moviedb, 
                    'movies': movies_moviedb,
                    'tvSeries': tvSeries_moviedb,
                    'formLog': formLog,
                    })

def cadastro(request):
    if not request.user.is_authenticated:

        formCad = CadastroForms()
        formLog = LoginForms()

        if request.method == 'POST':
            formCad = CadastroForms(request.POST)

            if formCad.is_valid():

                nome=formCad['nome_cadastro'].value()
                email=formCad['email'].value()
                senha=formCad['senha_1'].value()

                if User.objects.filter(username=nome).exists():
                    messages.error(request, f"Usuario já existente!")
                    return redirect('cadastro')

                usuario = User.objects.create_user(
                    username=nome,
                    email=email,
                    password=senha
                )
                usuario.save()
                messages.success(request, f"Cadastro efetuado com sucesso!")
                return redirect('index')

        return render(request, 'critics/cadastro.html', {'formLog': formLog,'formCad':formCad})
    
    else:
        messages.info(request, "Não pode acessar a tela de cadastro pois já está logado !")
        return redirect('index')

def movie(request,movieId):

    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('index')
    
    data_moviedb = moreMovie(movieId)
    cast_moviedb, crew_moviedb = castMovie(movieId)
    provider_moviedb = providersMovie(movieId)
    similar_moviedb = similarMovie(movieId)

    return render(request, 'critics/movie.html', 
                  {
                    'pageTitle':data_moviedb['title'] if data_moviedb else 'Pagina não encontrada',
                    'movie': data_moviedb,
                    'cast': cast_moviedb,
                    'crew': crew_moviedb,
                    'providers': provider_moviedb,
                    })

def tvSeries(request,tvSeriesId):
   
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('index')
    
    data_moviedb = moreTvSeries(tvSeriesId)
    cast_moviedb,crew_moviedb = castTvSeries(tvSeriesId)
    provider_moviedb = providersTvSeries(tvSeriesId)

    return render(request, 'critics/tvSeries.html', 
                  {
                    'pageTitle': f"TV Show - {data_moviedb['name']}" if data_moviedb else 'Pagina não encontrada',
                    'tvSeries': data_moviedb,
                    'cast': cast_moviedb,
                    'crew': crew_moviedb,
                    'providers': provider_moviedb,
                    'post':True,
                    'postType':'tvSeries',
                    'postInfo':data_moviedb,
                    }) 

def season(request,tvSeriesId,seasonNumber):
   
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('index')
    
    season_moviedb = moreSeason(tvSeriesId,seasonNumber)
    cast_moviedb = castSeason(tvSeriesId,seasonNumber)
    provider_moviedb = providersSeason(tvSeriesId,seasonNumber)

    return render(request, 'critics/season.html', 
                  {
                    'pageTitle': f"Temporada - {season_moviedb['name']}" if season_moviedb else 'Pagina não encontrada',
                    'tvSeriesId': tvSeriesId,
                    'season': season_moviedb,
                    'cast': cast_moviedb,
                    'providers': provider_moviedb,
                    }) 

def episode(request,tvSeriesId,seasonNumber,episodeNumber):
   
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('index')
    
    episode_moviedb = moreEpisode(tvSeriesId,seasonNumber,episodeNumber)
    cast_moviedb = castEpisode(tvSeriesId,seasonNumber,episodeNumber)
    provider_moviedb = providersSeason(tvSeriesId,seasonNumber)

    return render(request, 'critics/episode.html', 
                  {
                    'pageTitle': f"Episódio - {episode_moviedb['name']}" if episode_moviedb else 'Pagina não encontrada',
                    'tvSeriesId': tvSeriesId,
                    'seasonNumber': seasonNumber,
                    'episode': episode_moviedb,
                    'cast': cast_moviedb,
                    'providers': provider_moviedb,
                    }) 

def person(request,personId):

    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('index')
    
    data_moviedb = morePerson(personId)
    movies_moviedb = movieCreditsPerson(personId)
    tv_moviedb = TvCreditsPerson(personId)

    return render(request, 'critics/person.html', 
                  {
                    'person': data_moviedb,
                    'movies': movies_moviedb,
                    'tvSeries':tv_moviedb,
                    'post':True,
                    'postType':'person',
                    'postInfo':data_moviedb,
                    })

def search(request,page):
    formLog = LoginForms()
    searchText = request.POST.get('searchText')
    searchResults = searchMovieDb(searchText,page)
    return render(request, 'critics/search.html', 
                  {
                    'pageTitle': 'Pesquisa - Critics',
                    'searchText': searchText,
                    'results': searchResults,
                    'previousPage': (searchResults['page'] - 1) if searchResults['page'] != 1 else None,
                    'nextPage': (searchResults['page'] + 1) if searchResults['page'] != searchResults['total_pages'] else None,
                    'quant_results': len(searchResults['results']),
                    'formLog': formLog,
                    })

def trending(request):
    
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('index')
    
    movies_moviedb = trendingMovie()
    tvSeries_moviedb = trendingTvSeries()
    
    return render(request, 'critics/trending.html', 
                  {
                    'pageTitle': 'Trending - Critics',
                    'movies': movies_moviedb,
                    'tvSeries': tvSeries_moviedb,
                    })

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('index')