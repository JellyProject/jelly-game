from django.db import models

from .. import game_settings as constant


class Production(models.Model):
    """
    Production model

    Fields:
        money (int):
        hydrocarbons (int):
        food (int):
        electricity (int):
        pollution (int):
        waste (int):
    """
    player = models.OneToOneField('Player', on_delete=models.CASCADE)

    money = models.IntegerField(default=constant.UM_INITIAL_PRODUCTION)
    hydrocarbons = models.IntegerField(default=constant.HYDROCARBONS_INITIAL_PRODUCTION)
    food = models.IntegerField(default=constant.FOOD_INITIAL_PRODUCTION)
    electricity = models.IntegerField(default=constant.ELECTRICITY_INITIAL_PRODUCTION)
    pollution = models.IntegerField(default=constant.POLLUTION_INITIAL_PRODUCTION)
    waste = models.IntegerField(default=constant.WASTE_INITIAL_PRODUCTION)
