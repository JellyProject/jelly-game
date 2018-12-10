from django.db import models

from .. import game_settings as constant

from .technology import Technology
from .event import Event


class Game(models.Model):
    """
    Game model

    Attributes:
        players: query set of players in the game
        hydrocarbons_piles: query set of hydrocarbon piles in the game
        current_index_pile (int): index of the current pile
    """

    name = models.CharField(max_length=20, default="a")
    current_index_pile = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def _init_supply(self):
        """ Initialize the hydrocarbon supply piles """
        const = constant.HYDROCARBON_STOCKS_PER_PLAYER
        for pile_index in range(len(const)):
            HydrocarbonSupplyPile.objects.get_or_create(stock_amount=const[pile_index][0],
                                                        multiplier=const[pile_index][1],
                                                        index=pile_index, game=self)

    def save_game(self):
        """ Save the game state in the data base
        inutile ?? probablement xD"""
        for player in self.players:
            player.save()
        for pile in self.hydrocarbon_piles:
            pile.save()

    def add_player(self, user):
        """
           Adds a player in the game and updates the global hydrocarbon supplies
        """
        # Check if a player already has this name
        if not Player.objects.filter(game__name=self.name, user=user):
            new_player = Player.objects.create(game=self, user=user)
            Resources.objects.create(player=new_player)
            Production.objects.create(player=new_player)
            States.objects.create(player=new_player)
            # ajustement du stock mondial d'hydrocarbures
            const = constant.HYDROCARBON_STOCKS_PER_PLAYER
            for pile_index in range(len(const)):
                self.hydrocarbon_piles.get(index=pile_index).stock_amount += const[pile_index][0]
        else:    # For debugging purposes, should be deleted or modified
            print("A player already has this user name, sorry!")    # Print in console

    def update_index_pile(self):
        """ Update the index of the current pile """
        # if there is no more hydrocarbon in the current pile, change pile (while in case of problems)
        hydrocarbon_piles = self.hydrocarbon_piles.order_by('index')
        while hydrocarbon_piles[self.current_index_pile].stock_amount <= 0:
            self.current_index_pile += 1
            hydrocarbon_piles[self.current_index_pile].decrease(-hydrocarbon_piles[self.current_index_pile - 1]
                                                                .stock_amount)
            hydrocarbon_piles[self.current_index_pile - 1].setTo(0)
            # print(hydrocarbon_piles[self.current_index_pile - 1].stock_amount)
            hydrocarbon_piles[self.current_index_pile].save()
            hydrocarbon_piles[self.current_index_pile - 1].save()
        # print(hydrocarbon_piles[1].stock_amount)
        self.save()

    def income_phase(self):
        """ Income phase : each player gain his income """
        # income for each player
        for player in self.players.all():
            player.earn_income()
        # update of the current pile index
        self.update_index_pile()

    def main_phase(self):
        """ Main phase """
        pass
