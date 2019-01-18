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
    player = models.OneToOneField('Player', on_delete=models.CASCADE, editable=False)

    money = models.IntegerField(default=constant.UM_INITIAL_PRODUCTION)
    hydrocarbon = models.IntegerField(default=constant.HYDROCARBON_INITIAL_PRODUCTION)
    food = models.IntegerField(default=constant.FOOD_INITIAL_PRODUCTION)
    electricity = models.IntegerField(default=constant.ELECTRICITY_INITIAL_PRODUCTION)
    pollution = models.IntegerField(default=constant.POLLUTION_INITIAL_PRODUCTION)
    waste = models.IntegerField(default=constant.WASTE_INITIAL_PRODUCTION)

    def __str__(self):
        return "Production (Game : {0}, Player : {1})".format(self.player.game.name, self.player.username())

    class Meta:
        verbose_name = "Production"
        verbose_name_plural = "Production"

    def __eq__(self, other):
        return (self.player.id == other.player.id and
                self.money == other.money and
                self.hydrocarbon == other.hydrocarbon and
                self.food == other.food and
                self.electricity == other.electricity and
                self.pollution == other.pollution and
                self.waste == other.waste)
