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
    name = models.CharField(max_length=100)
    resources = models.OneToOneField(Resources, on_delete=models.CASCADE)
    production = models.OneToOneField(Production, on_delete=models.CASCADE)
    states = models.OneToOneField(States, on_delete=models.CASCADE)

    # Encore a traiter vv
    technologies = models.IntegerField(default=0)
    builded = models.IntegerField(default=0)

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
    stock_amount = models.IntegerField(default=0)
    multiplier = models.IntegerField(default=0)
    index = models.IntegerField()

    def decrease(self, diminution):
        """ Diminue le stock de diminution """
        self.stock_amount -= diminution
