import game.models as models


class Game():
    """
    Game class

    Atributes:
        players: query set of players in the game
        hydrocarbons_piles: query set of hydrocarbon piles in the game
        current_index_pile (int): index of the current pile
    """

    def __init__(self):
        """ Load the game from data base """
        self.players = models.Player.objects.all()
        self.hydrocarbon_piles = models.HydrocarbonSupplyPile.objects.order_by('index')
        self.current_index_pile = 0

        self.update_index_pile()

    def new_game(self):
        """ Create a new game deleting the previous one """
        self.players.delete()
        self.hydrocarbon_piles.delete()
        self.current_index_pile = 0
        self._init_supply()

    def _init_supply(self):
        """ Initialize the hydrocarbon supply piles """
        const = constant.HYDROCARBON_STOCKS_PER_PLAYER
        for pile_index in range(len(const)):
            models.HydrocarbonSupplyPile.objects.create(stock_amount=const[pile_index][0],
                                                        multiplier=const[pile_index][1], index=pile_index)

    def save_game(self):
        """ Save the game state in the data base """
        for player in self.players:
            player.save()
        for pile in self.hydrocarbon_piles:
            pile.save()

    def new_player(self, name):
        """ Add a player in the world, and hydrocarbon supply in consequence """
        # creation d'un nouveau joueur
        player = models.Player.objects.create(name=name, resources=Resources(), production=Production(), states=States)
        # ajustement du d'un stock mondial d'hydrocarbures en consequence
        const = constant.HYDROCARBON_STOCKS_PER_PLAYER
        for pile_index in range(len(const)):
            self.hydrocarbon_piles.get(index=pile_index).stock_amount += const[pile_index][0]

    def update_index_pile(self):
        """ Update the index of the current pile """
        # if there is no more hydrocarbon in the current pile, change pile (while in case of problems)
        while hydrocarbon_piles[self.current_index_pile].stock_amount <= 0:
            self.current_index_pile += 1
            self.hydrocarbon_piles[self.current_index_pile].stock_amount -= \
                hydrocarbon_piles[self.current_index_pile].stock_amount
            self.hydrocarbon_piles[self.current_index_pile - 1].stock_amount = 0

    def income_phase(self):
        """ Income phase : each player gain his income """
        # income for each player
        for player in self.players:
            player.earn_income()
        # update of the current pile index
        self.update_index_pile()

    def main_phase(self):
        """ Main phase """
        pass
