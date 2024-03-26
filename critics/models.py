from django.db import models

from datetime import datetime

from django.contrib.auth.models import User

class Post(models.Model):

    OPCOES_CATEGORIA = [
        ("MOVIE", "Filme"),
        ("TVSERIES", "Série de TV"),
        ("SEASON", "Temporada"),
        ("EPISODE", "Episódio"),
        ("PERSON", "Pessoa"),
    ]

    id_post = models.CharField(unique=True, max_length=20, null=False, blank=False)  
    id_movieDB = models.CharField(max_length=20, null=False, blank=False)
    type_movieDB = models.CharField(choices=OPCOES_CATEGORIA, max_length=10, null=False, blank=False)
    text_post = models.TextField(null=False, blank=False)
    data_post = models.DateTimeField(default=datetime.now, blank=False)
    publicado = models.BooleanField(default=True)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts",
    )

    def __str__(self):
        return f"Post {self.id} - {self.id_post} - {self.id_movieDB} - {self.text_post[:20]}... - {self.data_post.strftime('%Y/%m/%d')}"

class Review(models.Model):

    OPCOES_CATEGORIA = [
        ("MOVIE", "Filme"),
        ("TVSERIES", "Série de TV"),
        ("SEASON", "Temporada"),
        ("EPISODE", "Episódio"),
        ("PERSON", "Pessoa"),
    ]

    id_movieDB = models.CharField(max_length=20, null=False, blank=False)
    type_movieDB = models.CharField(choices=OPCOES_CATEGORIA, max_length=10, null=False, blank=False)
    image_movieDB = models.CharField(max_length=150, null=False, blank=False)
    text_review = models.TextField(null=False, blank=False)
    data_review = models.DateTimeField(default=datetime.now, blank=False)
    rate_review = models.IntegerField(default=1)
    publicado = models.BooleanField(default=True)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="reviews",
    )

    def __str__(self):
        return f"Review {self.id_movieDB}"
