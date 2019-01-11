from django.db import models

from .. import game_settings as constant


class Technology(models.Model):
    """
    Technology model

    Fields :
        player (ForeignKey -> Player) : The player who may own this technology.
        index (int) : A unique index to link this technology to a source technology.
        unlocked (bool) : True -> This technology may be purchased by the player.
        purchased (bool) : True -> This technology has been purchased by the player.
    """
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='technologies')
    index = models.IntegerField(unique=True)
    unlocked = models.BooleanField(default=False)
    purchased = models.BooleanField(default=False)
