from django.db import models

from .. import game_settings as constant


class PlayerBuilding(models.Model):
    """
    PlayerBuilding model

    Fields :
        player (ForeignKey -> Player) : Player associated with in a ForeignKey link

        index (int) : unique index for each building
        unlocked (bool) : True if player has unlocked this building, False else
        number_of (int) : number of buidings of this type owned by player
    """
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='buildings')

    index = models.IntegerField(editable=False)
    # unlockable = models.BooleanField(default=False) (surtout pour les techs)
    unlocked = models.BooleanField(default=False)
    number_of = models.IntegerField(default=0)

    def purchase(self):
        """
        Purchase of a copy of the building by player

        - Check if the building is unlocked, and if player has enough money to build it
        - Add 1 to number_of
        - Lower money, and apply the bukding modifiers to balance and production
        - Launch the building special effect
        """
        if not self.unlocked:
            print('This building is not unlocked yet !')
            return

        building = self.player.game.buildings.get(index=self.index)

        if (self.player.resources.money < building.cost):
            print('Not enough money to buy the buiding')
            return

        self.number_of += 1

        self.player.resources.money -= building.cost
        self.player.resources.save()

        self.player.production.money += building.money_modifier
        self.player.production.food += building.food_modifier
        self.player.production.hydrocarbon += building.hydrocarbon_modifier
        self.player.production.electricity += building.electricity_modifier
        self.player.production.pollution += building.pollution_modifier
        self.player.production.waste += building.waste_modifier
        self.player.production.save()

        self.player.balance.economic += building.economic_modifier
        self.player.balance.social += building.social_modifier
        self.player.balance.environmental += building.environement_modifier
        self.player.balance.save()
