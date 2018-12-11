from django.db import models

from .. import game_settings as constant


class HydrocarbonSupplyPile(models.Model):
    """
    Pile d'hydrocarbures

    Attributs :
        stocks : quantite d'hydrocarbures restant dans la pile
        multipliers : rendement de la pile
        index : numero de la pile
        supply_list : reserve generale dans laquelle se situe la pile
    """
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name="hydrocarbon_piles")
    stock_amount = models.FloatField(default=0)
    multiplier = models.IntegerField(default=0)
    index = models.IntegerField(editable=False)

    def __str__(self):
        return str(self.index)

    def decrease(self, diminution):
        """ Diminue le stock de diminution """
        self.stock_amount -= diminution
        self.save()

    def setTo(self, value):
        self.stock_amount = value
        self.save()
