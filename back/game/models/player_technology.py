from django.db import models

from .. import game_settings as constant

from .player import Player


class TechnologyPlayer(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='technologies')

    index = models.IntegerField(unique=True)
    unlockable = models.BooleanField(default=False)
    unlocked = models.BooleanField(default=False)
