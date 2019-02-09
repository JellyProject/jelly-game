from django.db import models

from .. import game_settings as constant


class ShadowPlayer(models.Model):
    """
    Shadow player model, modelize the action pile within each round for a Player

    Fields :
        * player (OneToOne -> Player)
        * state (OneToOne <- PlayerState)
    """
    player = models.OneToOneField('Player', on_delete=models.CASCADE, editable=False)
