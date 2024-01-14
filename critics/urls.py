from django.urls import path
from critics.views import index, movie, login

urlpatterns = [
    path('', index, name='index'),
    path('movie/<int:movieId>', movie, name='movie'),
    path('login', login, name='login'),
]