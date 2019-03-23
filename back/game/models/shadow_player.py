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

    def __str__(self):
        return "{0}'s shadow (Game : {1})".format(self.player.username, self.player.game.pk)

    @classmethod
    def create(cls, player):
        """
        Create and return a new Shadowplayer linked to a player

        Args :
            player (Player) : player to which the shadowplayer is linked
        """
        # source_building = models.SourceBuilding.objects.all()[0]
        new_shadowplayer = cls(player=player)
        new_shadowplayer.save()  # Peut-on faire mieux ?

        return new_shadowplayer

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