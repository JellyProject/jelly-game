from django.db import models

from .. import game_settings as constant


class Resources(models.Model):
    """
    Resources model

    Fields:
        player (OneToOne -> Player) : Player associated with in a OneToOne link
        money (int) : amount of money owned by player
        hydrocarbons (int) : amount of hydrocarbons owned by player
    """
    player = models.OneToOneField('Player', on_delete=models.CASCADE, related_name='resources')

    money = models.IntegerField(default=constant.UM_INITIAL_STOCK)
    hydrocarbons = models.IntegerField(default=constant.HYDROCARBONS_INITIAL_STOCK)
