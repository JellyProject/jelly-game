from django.db import models

import game.game_settings as constant


class Resources(models.Model):
    """
    Resources model

    Fields:
        um (int):
        hydrocarbons (int):
        pollution (int):
    """
    um = models.IntegerField(default=constant.UM_INITIAL_STOCK)
    hydrocarbons = models.IntegerField(default=constant.HYDROCARBONS_INITIAL_STOCK)
    pollution = models.IntegerField(default=constant.POLLUTION_INITIAL_STOCK)


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
    economical = models.IntegerField(default=constant.ECONOMICAL_INITIAL_VALUE)
    social = models.IntegerField(default=constant.SOCIAL_INITIAL_VALUE)
    environmental = models.IntegerField(default=constant.ENVIRONMENTAL_INITIAL_VALUE)

    def green_income(self):
        """ Return environment regeneration income corresponding to the environmental level """
        return self.environmental // constant.ENVIRONMENTAL_REGENERATION_LEVEL


class Game(models.Model):
    """
    Game model

    Attributes:
        players: query set of players in the game
        hydrocarbons_piles: query set of hydrocarbon piles in the game
        current_index_pile (int): index of the current pile
    """

    name = models.CharField(default="a", max_length=20)
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

    def new_player(self, name):
        """ Add a player in the world, and hydrocarbon supply in consequence """
        # creation d'un nouveau joueur s'il n'existe pas encore
        try:
            self.players.get(name=name)
        except:
            player = Player(name=name, game=self)
            player.resources = Resources.objects.create()
            player.production = Production.objects.create()
            player.state = States.objects.create()
            player.save()

            # ajustement du d'un stock mondial d'hydrocarbures en consequence
            const = constant.HYDROCARBON_STOCKS_PER_PLAYER
            for pile_index in range(len(const)):
                self.hydrocarbon_piles.get(index=pile_index).stock_amount += const[pile_index][0]

    def update_index_pile(self):
        """ Update the index of the current pile """
        # if there is no more hydrocarbon in the current pile, change pile (while in case of problems)
        hydrocarbon_piles = self.hydrocarbon_piles.order_by('index')
        while hydrocarbon_piles[self.current_index_pile].stock_amount <= 0:
            self.current_index_pile += 1
            hydrocarbon_piles[self.current_index_pile].stock_amount -= \
                hydrocarbon_piles[self.current_index_pile].stock_amount
            hydrocarbon_piles[self.current_index_pile - 1].stock_amount = 0
        hydrocarbon_piles.save()

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


class Player(models.Model):
    """
    Player model

    Fields:
        name (CharField): name of the player country
        resources (OneToOneField): Resources possessed by the player
        production (OneToOneField): player Production
        states (OneToOneField): player States
        technologies (OneToOneField?): technologies (not implemented yet)
        builded (OneToOneField?): building builded (not implemented yet)

    """
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="players")
    name = models.CharField(max_length=100, default="Anne O'NYME")
    resources = models.OneToOneField(Resources, on_delete=models.CASCADE)
    production = models.OneToOneField(Production, on_delete=models.CASCADE)
    states = models.OneToOneField(States, on_delete=models.CASCADE)

    # Encore a traiter vv
    technologies = models.IntegerField(default=0)
    builded = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def earn_income(self, hydrocarbon_stock):
        """
        Gain des revenus : um, hydrocarbures, pollution, et regeneration de l'envirronement
        """
        self.resources.um += self.production.um
        self.resources.pollution += self.production.pollution
        self.states.environmental += self.states.environmental.green_income()
        # Cas des hydrocarbures
        self.resources.hydrocarbons += self.production.hydrocarbons * hydrocarbon_stock.multiplier()
        hydrocarbon_stock.decrease(self.production.hydrocarbons)

    def green_income(self):
        return self.states.green_income()


class HydrocarbonSupplyPile(models.Model):
    """
    Pile d'hydrocarbures

    Attributs :
        stocks : quantite d'hydrocarbures restant dans la pile
        multipliers : rendement de la pile
        index : numero de la pile
        #supply_list : reserve generale dans laquelle se situe la pile
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
