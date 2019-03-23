from django.db import models

from .. import game_settings as constant


class Production(models.Model):
    """
    Production model

    Fields :
        * state (OneToOne -> PlayerState) : global state of the player related to the production

        * money (int) : money production of player at the beginning of each generation
        * hydrocarbon (int) : hydrocarbon points production of player at the beginning of each generation
        * hydrocarbon_consumption (int) : hydrocarbon ressources coonsumption of player buildings

        * food (int) : unused food production of player at the beginning of each generation
        * electricity (int) : unused electricity production of player at the beginning of each generation

        * pollution (int) : untreated pollution production of player at the beginning of each generation
        * waste (int) : untreated waste production of player at the beginning of each generation
    """
    state = models.OneToOneField('PlayerState', on_delete=models.CASCADE, related_name='production', editable=False)

    money = models.IntegerField(default=constant.UM_INITIAL_PRODUCTION)
    hydrocarbon = models.IntegerField(default=constant.HYDROCARBON_INITIAL_PRODUCTION)
    hydrocarbon_consumption = models.IntegerField(default=constant.HYDROCARBON_INITIAL_CONSUMPTION)
    food = models.IntegerField(default=constant.FOOD_INITIAL_PRODUCTION)
    electricity = models.IntegerField(default=constant.ELECTRICITY_INITIAL_PRODUCTION)
    pollution = models.IntegerField(default=constant.POLLUTION_INITIAL_PRODUCTION)
    waste = models.IntegerField(default=constant.WASTE_INITIAL_PRODUCTION)


    def __str__(self):
        return "{0}'s production (Game : {1})".format(self.player.username, self.player.game.pk)

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

    @property
    def player(self):
        return self.state.player
