from django.db import models

from .. import game_settings as settings


class Resources(models.Model):
    """
    Resources model

    Fields:
        player (OneToOne -> Player) : Player associated with in a OneToOne link
        money (int) : amount of money owned by player
        hydrocarbon (int) : amount of hydrocarbon owned by player
    """
    player = models.OneToOneField('Player', on_delete=models.CASCADE, related_name='resources', editable=False)
    money = models.IntegerField(default=settings.UM_INITIAL_STOCK)
    hydrocarbon = models.IntegerField(default=settings.HYDROCARBON_INITIAL_STOCK)

    def __str__(self):
        return "Resources (Game : {0}, Player : {1})".format(self.player.game.pk, self.player.username())

    class Meta:
        verbose_name = "Resources"
        verbose_name_plural = "Resources"

    def __eq__(self, other):
        return (self.player.id == other.player.id and
                self.money == other.money and
                self.hydrocarbon == other.hydrocarbon)
