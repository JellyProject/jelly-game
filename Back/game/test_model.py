from django.db import models

import game_settings as constant


class Resources(models.Model):
    um = models.IntegerField(default=constant.UM_INITIAL_STOCK)
    hydrocarbons = models.IntegerField(default=constant.HYDROCARBONS_INITIAL_STOCK)
    pollution = models.IntegerField(default=constant.POLLUTION_INITIAL_STOCK)


class Production(models.Model):
    um = models.IntegerField(default=constant.UM_INITIAL_PRODUCTION)
    hydrocarbons = models.IntegerField(default=constant.HYDROCARBONS_INITIAL_PRODUCTION)
    food = models.IntegerField(default=constant.FOOD_INITIAL_PRODUCTION)
    electricity = models.IntegerField(default=constant.ELECTRICITY_INITIAL_PRODUCTION)
    pollution = models.IntegerField(default=constant.POLLUTION_INITIAL_PRODUCTION)
    waste = models.IntegerField(default=constant.WASTE_INITIAL_PRODUCTION)


class States(models.Model):
    economical = models.IntegerField(default=constant.ECONOMICAL_INITIAL_VALUE)
    social = models.IntegerField(default=constant.SOCIAL_INITIAL_VALUE)
    environmental = models.IntegerField(default=constant.ENVIRONMENTAL_INITIAL_VALUE)

    def green_income(self):
        return self.environmental // constant.ENVIRONMENTAL_REGENERATION_LEVEL


class Player(models.Model):
    """
    Classe principale joueur
    """
    name = models.CharField(max_length=100)
    resources = models.OneToOneField(Resources, on_delete=models.CASCADE)
    
    world = models.ForeignKey(World, on_delete=models.CASCADE)
    production = models.OneToOneField(Production, on_delete=models.CASCADE)
    states = models.OneToOneField(States, on_delete=models.CASCADE)

    # Encore a traiter vv
    technologies = models.IntegerField(default=0)
    buildes = models.IntegerField(default=0)

    def earn_income(self, hydrocarbon_stock):
        """
        Gain des revenus : um, hydrocarbures, pollution, et regeneratinon de l'envirronement
        """
        self.resources.um += self.production.um
        self.resources.pollution += self.production.pollution
        self.states.environmental += self.states.environmental.green_income()
        # Cas des hydrocarbures
        self.resources.hydrocarbons += self.production.hydrocarbons * hydrocarbon_stock.multiplier()
        hydrocarbon_stock.decrease(self.production.hydrocarbons)

# A renommer
class Hydrocarbon_stock(models.Model):
    stock = models.IntegerField(default=0)
    multiplier = models.IntegerField(default=0)
    index = models.IntegerField()
    stock_list = models.ForeignKey(Hydrocarbon_stocks, on_delete=models.CASCADE)

    def decrease(self, diminution):
        """ Diminue le stock de diminution """
        self.stocks -= diminution


class Hydrocarbon_stocks(models.Model):
    """
    Reserves mondiales d'hydrocarbures

    Attributs :
        stocks_piles_list : liste du stock courant de chaque pile
        multipliers_list : liste des multiplicateurs associes a chaque pile
        current_multiplier_index : indice actuel du stock sur lequel on preleve
    """
    def __init__(self):
        """ Constructeur d'un stock vide """
        number_of_stock_piles = len(constant.HYDROCARBON_STOCKS_PER_PLAYER)
        self.stocks_piles_list = [0 for i in range(number_of_stock_piles)]
        self.multipliers_list = [0 for i in range(number_of_stock_piles)]
        self.current_multiplier_index = 0

    def add_country(self):
        """ Ajoute un stock pour un pays """
        for i_stock in range(len(self.stocks_list)):
            self.stocks_piles_list[i_stock] += constant.HYDROCARBON_STOCKS_PER_PLAYER[i_stock][0]
            self.multipliers_list[i_stock] += constant.HYDROCARBON_STOCKS_PER_PLAYER[i_stock][1]

    # @property fonctionne-t-il si multiplier n'est pas un attribut ?? (a tester par curiosite)
    def multiplier(self):
        """ Renvoie le multiplicateur courant """
        return self.multipliers_list[self.current_multiplier_index]

    def update_multiplier(self):
        """ Met a jour le multiplicateur courant """
        if self.stocks_piles_list[self.current_multiplier_index] <= 0:
            self.current_multiplier_index += 1
            # On retire l'excedent en negatif
            self.stocks_piles_list[current_multiplier_index] += self.stocks_piles_list[current_multiplier_index - 1]

    def decrease(self, diminution):
        """ Diminue le stock de diminution """
        self.stocks_piles_list[self.current_multiplier_index] -= diminution


class World(models.Model):
    """ Monde/jeu """
    def __init__(self):
        """ Construction d'un monde vide """
        self.players = []
        self.hydrocarbon_stock = Hydrocarbon_stock()

    def add_country(self, name):
        """ Ajout et creation d'un joueur/pays dans le monde """
        # creation d'un nouveau joueur
        self.players.append(Player(name))
        # ajustement du d'un stock mondial d'hydrocarbures en consequence
        self.hydrocarbon_stock.add_country()

    def income_phase(self):
        """ Phase de revenus """
        # mise a jour du multiplicateur pour cette phase
        self.hydrocarbon_stock.update_multiplier()
        for player in self.players:
            player.earn_income(self.hydrocarbon_stock)

    def main_phase(self):
        pass
