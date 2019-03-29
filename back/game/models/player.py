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

        * shadow (OneToOne <- ShadowPlayer)
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
        Create and return a new Player linked to profile in game

        Args :
            * profile (Profile) : profile which will control this player
            * game (Game) : game in which the player will play
        """
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
        self.balance.environmental -= self.production.waste
        self.balance.green_income()  # environment generation income

        # Cas des hydrocarbures
        hydrocarbon_stock = self.game.hydrocarbon_piles.get(index=self.game.current_index_pile)
        self.resources.hydrocarbon += self.production.hydrocarbon * hydrocarbon_stock.multiplier
        hydrocarbon_stock.decrease(self.production.hydrocarbon * hydrocarbon_stock.multiplier)
        self.resources.hydrocarbon -= self.production.hydrocarbon_consumption

        # importations of missing resources
        if self.production.food < 0:
            self.resources.money += self.production.food * constant.IMPORTATION_COST
        if self.production.electricity < 0:
            self.production.money += self.production.electricity * constant.IMPORTATION_COST
        if self.resources.hydrocarbon < 0:
            self.resources.money += self.resources.hydrocarbon * constant.IMPORTATION_COST
            self.resources.hydrocarbon = 0

        self.resources.save()
        self.balance.save()

    def update(self):
        """ Copy shadow in player """
        self.state.balance.economic = self.shadow.state.balance.economic
        self.state.balance.social = self.shadow.state.balance.social
        self.state.balance.environmental = self.shadow.state.balance.environmental
        self.state.balance.save()

        self.state.resources.money = self.shadow.state.resources.money
        self.state.resources.hydrocarbon = self.shadow.state.resources.hydrocarbon
        self.resources.save()

        self.state.production.money = self.shadow.production.money
        self.state.production.hydrocarbon = self.shadow.production.hydrocarbon
        self.state.production.hydrocarbon_consumption = self.shadow.production.hydrocarbon_consumption
        self.state.production.food = self.shadow.production.food
        self.state.production.electricity = self.shadow.production.electricity
        self.state.production.pollution = self.shadow.production.pollution
        self.state.production.waste = self.shadow.production.waste
        self.production.save()

        for building in self.state.buildings.all():
            building.unlocked = Building.objects.get(source=building.source, state=self.shadow.state).unlocked
            building.copies = Building.objects.get(source=building.source, state=self.shadow.state).copies
            building.quantity_cap = Building.objects.get(source=building.source, state=self.shadow.state).quantity_cap
            building.save()

        for technology in self.state.technologies.all():
            technology.unlocked = Technology.objects.get(source=technology.source, state=self.shadow.state).unlocked
            technology.purchased = Technology.objects.get(source=technology.source, state=self.shadow.state).purchased
            technology.save()
