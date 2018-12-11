from django.db import models

from .. import game_settings as constant

from .player import Player


class BuildingPlayer(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='buildings')

    index = models.IntegerField(editable=False)
    # unlockable = models.BooleanField(default=False) (surtout pour les techs)
    unlocked = models.BooleanField(default=False)
    number_of = models.IntegerField(default=0)

    def purchase(self):
        if not self.unlocked:
            print('This building is not unlocked yet !')
            return

        self.number_of += 1
        building = self.player.game.buildings.get(index=self.index)

        if (self.player.resources.money < building.cost):
            print('Not enough money to buy the buiding')
            return
        self.player.resources.money -= building.cost
        self.player.resources.save()

        self.player.production.money += building.money_modifier
        self.player.production.food += building.food_modifier
        self.player.production.hydrocarbons += building.hydrocarbon_modifier
        self.player.production.electricity += building.electricity_modifier
        self.player.production.pollution += building.pollution_modifier
        self.player.production.waste += building.waste_modifier
        self.player.production.save()

        self.player.states.economical += building.economic_modifier
        self.player.states.social += building.social_modifier
        self.player.states.environmental += building.environement_modifier
        self.player.states.save()
