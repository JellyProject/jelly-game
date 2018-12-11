from django.db import models

from .. import game_settings as constant

# from .player import Player


class Resources(models.Model):
    """
    Resources model

    Fields:
        money (int):
        hydrocarbons (int):
        pollution (int):
    """
    player = models.OneToOneField('Player', on_delete=models.CASCADE, related_name='resources')

    money = models.IntegerField(default=constant.UM_INITIAL_STOCK)
    hydrocarbons = models.IntegerField(default=constant.HYDROCARBONS_INITIAL_STOCK)
    # pollution = models.IntegerField(default=constant.POLLUTION_INITIAL_STOCK)

    class Meta:
        app_label = 'game'
