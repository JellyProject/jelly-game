from django.db import models

from .. import game_settings as constant


class PlayerTechnology(models.Model):
    """
    TechnologyPlyer model

    Fields :
        player (ForeignKey -> Player) : Player associated with in a ForeignKey link

        index (int) : unique index for each technology
        unlockable (bool) : True if player can unlock this technology, False else
        unlocked (bool) : True if player has unlocked this technology, False else
    """
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='technologies')

    index = models.IntegerField(unique=True)
    unlockable = models.BooleanField(default=False)
    unlocked = models.BooleanField(default=False)
