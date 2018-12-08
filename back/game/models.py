from django.db import models

import game.game_settings as constant


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
        inutile ?? """
        for player in self.players:
            player.save()
        for pile in self.hydrocarbon_piles:
            pile.save()

    def add_player(self, name):
        """
           Adds a player in the game and updates the global hydrocarbon supplies
        """
        # Check if a player already has this name
        if not Player.objects.filter(game__name=self.name, name=name):
            new_player = Player.objects.create(game=self, name=name)
            Resources.objects.create(player=new_player),
            Production.objects.create(player=new_player),
            States.objects.create(player=new_player)
            # ajustement du stock mondial d'hydrocarbures
            const = constant.HYDROCARBON_STOCKS_PER_PLAYER
            for pile_index in range(len(const)):
                self.hydrocarbon_piles.get(index=pile_index).stock_amount += const[pile_index][0]
        else:    # For debugging purposes, should be deleted or modified
            print("A player already has this name, sorry!")    # Print in console

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


class Player(models.Model):
    """
    Player model

    Fields:
        name (CharField): name of the player country
        resources (OneToOneField): Resources possessed by the player
        production (OneToOneField): player Production
        states (OneToOneField): player States
        technologies (OneToOneField?): technologies (not implemented yet)
        built (OneToOneField?): building built (not implemented yet)
    """
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="players")
    name = models.CharField(max_length=100, default="Anne O'NYME")

    # Encore a traiter vv
    technologies = models.IntegerField(default=0)
    builded = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def earn_income(self):
        """
        Gain des revenus : um, hydrocarbures, pollution, et regeneration de l'envirronement
        """
        self.resources.um += self.production.um
        self.states.environmental -= self.production.pollution
        self.green_income()
        # Cas des hydrocarbures
        hydrocarbon_stock = self.game.hydrocarbon_piles.get(index=self.game.current_index_pile)
        self.resources.hydrocarbons += self.production.hydrocarbons * hydrocarbon_stock.multiplier
        hydrocarbon_stock.decrease(self.production.hydrocarbons * hydrocarbon_stock.multiplier)
        self.resources.save()
        self.states.save()

    def green_income(self):
        self.states.green_income()


class Resources(models.Model):
    """
    Resources model

    Fields:
        um (int):
        hydrocarbons (int):
        pollution (int):
    """
    player = models.OneToOneField(Player, on_delete=models.CASCADE)

    um = models.IntegerField(default=constant.UM_INITIAL_STOCK)
    hydrocarbons = models.IntegerField(default=constant.HYDROCARBONS_INITIAL_STOCK)
    # pollution = models.IntegerField(default=constant.POLLUTION_INITIAL_STOCK)


class Production(models.Model):
    """
    Production model

    Fields:
        um (int):
        hydrocarbons (int):
        food (int):
        electricity (int):
        pollution (int):
        waste (int):
    """
    player = models.OneToOneField(Player, on_delete=models.CASCADE)

    um = models.IntegerField(default=constant.UM_INITIAL_PRODUCTION)
    hydrocarbons = models.IntegerField(default=constant.HYDROCARBONS_INITIAL_PRODUCTION)
    food = models.IntegerField(default=constant.FOOD_INITIAL_PRODUCTION)
    electricity = models.IntegerField(default=constant.ELECTRICITY_INITIAL_PRODUCTION)
    pollution = models.IntegerField(default=constant.POLLUTION_INITIAL_PRODUCTION)
    waste = models.IntegerField(default=constant.WASTE_INITIAL_PRODUCTION)


class States(models.Model):
    """
    States wheel model

    Fields:
        economical (int): economical level between 0 and constant.MAX_STATE_VALUE
                            initial value : constant.ECONOMICAL_INITIAL_VALUE
        social (int): social level between 0 and constant.MAX_STATE_VALUE
                        initial value : constant.SOCIAL_INITIAL_VALUE
        environmental (int): environmental level between 0 and constant.MAX_STATE_VALUE
                        initial value : constant.ENVIRONMENTAL_INITIAL_VALUE
    """
    player = models.OneToOneField(Player, on_delete=models.CASCADE)

    economical = models.IntegerField(default=constant.ECONOMICAL_INITIAL_VALUE)
    social = models.IntegerField(default=constant.SOCIAL_INITIAL_VALUE)
    environmental = models.IntegerField(default=constant.ENVIRONMENTAL_INITIAL_VALUE)

    def green_income(self):
        """ Return environment regeneration income corresponding to the environmental level """
        self.environmental += self.environmental // constant.ENVIRONMENTAL_REGENERATION_LEVEL
        self.environmental = min(self.environmental, 100)
        self.save()


class HydrocarbonSupplyPile(models.Model):
    """
    Pile d'hydrocarbures

    Attributs :
        stocks : quantite d'hydrocarbures restant dans la pile
        multipliers : rendement de la pile
        index : numero de la pile
        supply_list : reserve generale dans laquelle se situe la pile
    """
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="hydrocarbon_piles")
    stock_amount = models.FloatField(default=0)
    multiplier = models.IntegerField(default=0)
    index = models.IntegerField()

    def __str__(self):
        return str(self.index)

    def decrease(self, diminution):
        """ Diminue le stock de diminution """
        self.stock_amount -= diminution
        self.save()

    def setTo(self, value):
        self.stock_amount = value
        self.save()
