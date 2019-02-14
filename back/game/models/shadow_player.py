from django.db import models

from .. import game_settings as constant


class ShadowPlayer(models.Model):
    """
    Shadow player model, modelize the action pile within each round for a Player

    Fields :
        * player (OneToOne -> Player)
        * state (OneToOne <- PlayerState)
    """
    player = models.OneToOneField('Player', on_delete=models.CASCADE, editable=False)

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
        return self.state.purchase_building(slug)

    def purchase_technology(self, slug):
        return self.state.purchase_technology(slug)

    def recover(self, player):
        self.state = player.state