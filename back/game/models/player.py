from django.db import models

from .. import game_settings as constant

from .resources import Resources
from .production import Production
from .balance import Balance
from .building import Building
from .technology import Technology
from .source_building import SourceBuilding
from .source_technology import SourceTechnology
from .player_state import PlayerState

from .shadow_player import ShadowPlayer


class Player(models.Model):
    """
    Player model

    New fields :
        * game (Game) : ForeignKey link to the game in which the player plays
        * profile (Profile) : profile which controls the player
        * state (OneToOne <- PlayerState)
    """
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name="players", editable=False)
    profile = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name="players", editable=False)

    def __str__(self):
        return "{0} (Game : {1})".format(self.username, self.game.pk)

    def __eq__(self, other):
        return (self.game.id == other.game.id and
                self.profile.id == other.profile.id)

    @classmethod
    def create(cls, profile, game):
        """
        Create and return a new Player of profile in game

        Args :
            profile (Profile) : profile which will control this player
            game (Game) : game in which the player will play
        """
        # source_building = models.SourceBuilding.objects.all()[0]
        new_player = cls(game=game, profile=profile)
        new_player.save()  # Peut-on faire mieux ?
        player_state = PlayerState.create(new_player)
        shadow_player = ShadowPlayer.create(new_player)
        


        return new_player

    @property
    def username(self):
        """ Return the username of this player. """
        return self.profile.user.username

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

    def earn_income(self):
        """
        Apply the (beginning of generation) income phase to player

        Adjust money, hydrocarbon, and environment balance
        """
        self.resources.money += self.production.money
        self.balance.environmental -= self.production.pollution
        self.green_income()
        # Cas des hydrocarbures
        hydrocarbon_stock = self.game.hydrocarbon_piles.get(index=self.game.current_index_pile)
        self.resources.hydrocarbon += self.production.hydrocarbon * hydrocarbon_stock.multiplier
        hydrocarbon_stock.decrease(self.production.hydrocarbon * hydrocarbon_stock.multiplier)

        self.resources.save()
        self.balance.save()

    def green_income(self):
        """ Apply the environment generation income to the environment balance """
        self.balance.green_income()

    def purchase_building(self, slug):
        return self.state.purchase_building(slug)

    def purchase_technology(self, slug):
        return self.state.purchase_technology(slug)

    def clonage(self, shadow_player):
        self.state = shadow_player.state