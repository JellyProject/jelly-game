from django.db import models

from .. import game_settings as constant

from .game import Game


class GameEvent(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="events")
