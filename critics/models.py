from django.db import models

from datetime import datetime

from django.contrib.auth.models import User

class Post(models.Model):

    id_movieDB = models.CharField(max_length=20, null=False, blank=False)
    image_movieDB = models.CharField(max_length=150, null=False, blank=False)
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
        return f"Post {self.id_movieDB}"
