from django.db import models

from .. import game_settings as constant


class Production(models.Model):
    """
    Production model

    Fields :
        player (OneToOne -> Player) : Player associated with in a OneToOne link

        money (int) : money production of player at the beginning of each generation
        hydrocarbon (int) : hydrocarbon production of player at the beginning of each generation

        food (int) : unused food production of player at the beginning of each generation
        electricity (int) : unused electricity production of player at the beginning of each generation

        pollution (int) : untreated pollution production of player at the beginning of each generation
        waste (int) : untreated waste production of player at the beginning of each generation
    """
    player = models.OneToOneField('Player', on_delete=models.CASCADE)

    money = models.IntegerField(default=constant.UM_INITIAL_PRODUCTION)
    hydrocarbon = models.IntegerField(default=constant.HYDROCARBON_INITIAL_PRODUCTION)
    food = models.IntegerField(default=constant.FOOD_INITIAL_PRODUCTION)
    electricity = models.IntegerField(default=constant.ELECTRICITY_INITIAL_PRODUCTION)
    pollution = models.IntegerField(default=constant.POLLUTION_INITIAL_PRODUCTION)
    waste = models.IntegerField(default=constant.WASTE_INITIAL_PRODUCTION)
