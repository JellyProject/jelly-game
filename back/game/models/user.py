from django.db import models

from .. import game_settings as constant


# !! vaudrait mieux utiliser la classe user deja toute faite de django, avec une classe intermediaire Profile
class User(models.Model):
    name = models.CharField(max_length=constant.MAX_LENGTH_USER_NAME, default=constant.DEFAULT_USER_NAME)
    email = models.EmailField()
