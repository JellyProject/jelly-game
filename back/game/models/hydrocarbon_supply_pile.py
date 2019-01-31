from django.db import models

from .. import game_settings as constant


class HydrocarbonSupplyPile(models.Model):
    """
    HydrocarbonSupplyPile model

    Fields :
        game (ForeignKey -> Game) : game associated to this pile
        stock_amount (int) : amount of hydrocarbon left in the supply pile
        multiplier (int) : efficiency of the pile
        index (int) : index of the pile, is unique and indicate the order in which piles are drained
    """
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name="hydrocarbon_piles", editable=False)
    stock_amount = models.FloatField(default=0)
    multiplier = models.IntegerField(default=0)
    index = models.IntegerField(editable=False)

    def __str__(self):
        return "Pile n°{0} (Game : {1})".format(self.index, self.game.pk)

    def decrease(self, diminution):
        """ Decrease the stock_amount by diminution """
        self.stock_amount -= diminution
        self.save()

    def set_to(self, value):
        """ Set the stock_amount to value """
        self.stock_amount = value
        self.save()

    def is_empty(self):
        """ Check if the pile is empty ie if stock_amount <= 0 """
        if self.stock_amount <= 0:
            return True
        return False
