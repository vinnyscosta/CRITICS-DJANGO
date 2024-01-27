from django.urls import path
from critics.views import index, movie, logout

urlpatterns = [
    path('', index, name='index'),
    path('movie/<int:movieId>', movie, name='movie'),
    path('logout', logout, name='logout'),
]