import requests
from django.shortcuts import render, redirect
from critics.movieFunctions import *
from django.contrib import auth, messages
from critics.forms import LoginForms

def index(request):
    print(request.user)

    data_moviedb = discover()

    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()

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

    return render(request, 'critics/index.html', {'movies': data_moviedb,"form": form})

def movie(request,movieId):
    
    data_moviedb = movieMore(movieId)
    cast_moviedb = castMovie(movieId)

    return render(request, 'critics/movie.html', {'movie': data_moviedb,'cast': cast_moviedb,})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('index')