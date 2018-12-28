from django.db import models

from .. import game_settings as constant

from .technology import Technology
from .event import Event

from .player import Player
from .player_resources import Resources
from .player_production import Production
from .player_balance import Balance
from .game_hydrocarbon_supply_pile import HydrocarbonSupplyPile


class Game(models.Model):
    """
    Game model, representing a "world"

    Fields :
        name (string) : name of the game
        current_index_pile (int) : index of the current hydrocarbon pile in which players take ressources
        events :
        events :
        buildings :
        technologies :

        players (ForeignKey <- Player) : query set ofplayers in the game
        hydrocarbon_piles (ForeignKey <- HydrocarbonSupplyPile) : query set of hydrocarbon supply piles in the game
    """

    name = models.CharField(max_length=20, default="A random game")
    current_index_pile = models.IntegerField(default=0)
    # events = models.ManyToManyField('Event', on_delete=models.CASCADE)
    # buildings = models.ManyToManyField('Building', on_delete=models.CASCADE)
    # technologies = models.ManyToManyField('Technology', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name):
        """
        Create a new Game

        Args :
            name (string) : name of the new game
        """
        game = cls(name=name)
        game.save()
        game._init_supply()
        game.save()
        return game

    def _init_supply(self):
        """ Initialize the hydrocarbon supply piles """
        const = constant.HYDROCARBON_STOCKS_PER_PLAYER
        for pile_index in range(len(const)):
            HydrocarbonSupplyPile.objects.get_or_create(stock_amount=0,
                                                        multiplier=const[pile_index][1],
                                                        index=pile_index, game=self)

    def save_game(self):
        """ Save the game state in the data base
        inutile ?? probablement xD"""
        for player in self.players:
            player.save_player()
        for pile in self.hydrocarbon_piles:
            pile.save()

    def add_player(self, profile):
        """
        Adds a player in the game and updates the global hydrocarbon supplies accordingly

        Args :
            profile (Profile) : profile controlling the new player
        """
        # Check if a player already has this profile
        if not Player.objects.filter(game__name=self.name, profile=profile):
            # new_player = Player.objects.create(game=self, user=user)
            # Resources.objects.create(player=new_player)
            # Production.objects.create(player=new_player)
            # Balance.objects.create(player=new_player)
            new_player = Player.create(profile=profile, game=self)
            # ajustement du stock mondial d'hydrocarbures
            const = constant.HYDROCARBON_STOCKS_PER_PLAYER
            for pile_index in range(len(const)):
                self.hydrocarbon_piles.get(index=pile_index).decrease(-const[pile_index][0])
        else:    # For debugging purposes, should be deleted or modified
            print("A player already has this user name, sorry!")    # Print in console

    def update_index_pile(self):
        """ Update the index of the current hydrocarbon supply pile """
        # if there is no more hydrocarbon in the current pile, change pile (while in case of problems)
        hydrocarbon_piles = self.hydrocarbon_piles.order_by('index')
        while hydrocarbon_piles[self.current_index_pile].is_empty():
            self.current_index_pile += 1
            overflow = -hydrocarbon_piles[self.current_index_pile - 1].stock_amount
            hydrocarbon_piles[self.current_index_pile].decrease(overflow)
            hydrocarbon_piles[self.current_index_pile - 1].set_to(0)
        self.save()

    def income_phase(self):
        """ Run income phase for each player"""
        # income for each player
        for player in self.players.all():
            player.earn_income()
        # update of the current pile index
        self.update_index_pile()

    def main_phase(self):
        """ Main phase """
        pass
