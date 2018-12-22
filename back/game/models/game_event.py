from django.db import models

from .. import game_settings as constant


class GameEvent(models.Model):
    """
    GameEvent model

    Fields :
        game (ForeignKey -> Game) :
    """
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name="events")
