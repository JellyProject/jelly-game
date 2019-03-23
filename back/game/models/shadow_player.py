from django.db import models

from .. import game_settings as constant

from .player_state import PlayerState


class ShadowPlayer(models.Model):
    """
    Shadow player model, modelize the action pile within each round for a Player

    Fields :
        * player (OneToOne -> Player) : corresponding Player
        * state (OneToOne <- PlayerState) : corresponding PlayerState
    """
    player = models.OneToOneField('Player', on_delete=models.CASCADE, editable=False, related_name='shadow')

    def __str__(self):
        return "{0}'s shadow (Game : {1})".format(self.player.username, self.player.game.pk)

    @classmethod
    def create(cls, player):
        """
        Create and return a new Shadowplayer linked to a player

        Args :
            * player (Player) : player to which the shadowplayer is linked
        """
        new_shadowplayer = cls(player=player)
        new_shadowplayer.save()
        shadow_state = PlayerState.create(new_shadowplayer)
        return new_shadowplayer

    @property
    def game(self):
        """ Return the game in which the player plays """
        return self.player.game

    @property
    def resources(self):
        """ Return the resources of this player. """
        return self.state.resources

    @property
    def production(self):
        """ Return the production of this player. """
        return self.state.production

    @property
    def balance(self):
        """ Return the balance of this player. """
        return self.state.balance

    @property
    def buildings(self):
        """ Return the buildings of this player. """
        return self.state.buildings

    @property
    def technologies(self):
        """ Return the technologies of this player. """
        return self.state.technologies

    def purchase_building(self, slug):
        """ Purchase the building with given slug if possible. If not, return an error string. """
        return self.state.purchase_building(slug)

    def purchase_technology(self, slug):
        """ Purchase the technology with given slug if possible. If not, return an error string. """
        return self.state.purchase_technology(slug)

    def reset(self):
        """ Copy player to shadow_player """
        self.state.balance.economic = self.player.state.balance.economic
        self.state.balance.social = self.player.state.balance.social
        self.state.balance.environmental = self.player.state.balance.environmental
        self.state.balance.save()

        self.state.resources.money = self.player.state.resources.money
        self.state.resources.hydrocarbon = self.player.state.resources.hydrocarbon
        self.resources.save()

        self.state.production.money = self.player.production.money
        self.state.production.hydrocarbon = self.player.production.hydrocarbon
        self.state.production.hydrocarbon_consumption = self.player.production.hydrocarbon_consumption
        self.state.production.food = self.player.production.food
        self.state.production.electricity = self.player.production.electricity
        self.state.production.pollution = self.player.production.pollution
        self.state.production.waste = self.player.production.waste
        self.production.save()

        for building in self.state.buildings.all():
            building.unlocked = Building.objects.get(source=building.source, state=self.player.state).unlocked
            building.copies = Building.objects.get(source=building.source, state=self.player.state).copies
            building.quantity_cap = Building.objects.get(source=building.source, state=self.player.state).quantity_cap
            building.save()

        for technology in self.state.technologies.all():
            technology.unlocked = Technology.objects.get(source=technology.source, state=self.player.state).unlocked
            technology.purchased = Technology.objects.get(source=technology.source, state=self.player.state).purchased
            technology.save()
