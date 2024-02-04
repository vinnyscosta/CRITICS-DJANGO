import requests
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from critics.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User
from critics.movieFunctions import *
from critics.personFunctions import *

def index(request):
    print(request.user)

    data_moviedb = discoverMovie()

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

def cadastro(request):
    if not request.user.is_authenticated:

        form = CadastroForms()

        if request.method == 'POST':
            form = CadastroForms(request.POST)

            if form.is_valid():

                nome=form['nome_cadastro'].value()
                email=form['email'].value()
                senha=form['senha_1'].value()

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

        return render(request, 'critics/cadastro.html', {'form': form})
    
    else:
        messages.info(request, "Não pode acessar a tela de cadastro pois já está logado !")
        return redirect('index')

def movie(request,movieId):

    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('index')
    
    data_moviedb = moreMovie(movieId)
    cast_moviedb = castMovie(movieId)
    provider_moviedb = providersMovie(movieId)

    return render(request, 'critics/movie.html', {'movie': data_moviedb,'cast': cast_moviedb,'providers': provider_moviedb,})

def person(request,personId):

    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('index')
    
    data_moviedb = morePerson(personId)
    movies_moviedb = movieCreditsPerson(personId)

    return render(request, 'critics/person.html', {'person': data_moviedb,'movies': movies_moviedb,})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('index')