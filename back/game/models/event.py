from django.db import models

from .. import game_settings as constant


class Event(models.Model):
    name = models.CharField(max_length=40, unique=True, default="Ragnarok")
    version = models.CharField(max_length=20, default='jelly')  # Version of the game
    description = models.TextField(default='Today will be a sunny day.')
