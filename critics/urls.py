from django.urls import path
from critics.views import index, movie, person, logout

urlpatterns = [
    path('', index, name='index'),
    path('movie/<int:movieId>', movie, name='movie'),
    path('person/<int:personId>', person, name='person'),
    path('logout', logout, name='logout'),
]