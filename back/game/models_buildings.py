from django.db import models

import game.game_settings as constant
from game.models import Player, Game, Resources, Production, States, HydrocarbonSupplyPile


class Buildings(models.Model):
    pass


class Building(models.Model):
    pass


class BuildingsPlayer(models.Model):
    models.OneToOneField(Player, on_delete=models.CASCADE)


class BuildingPlayer(models.Model):
    models.ForeignKey(BuildingsPlayer, on_delete=models.CASCADE, related_name=buildings)
    index = models.IntegerField(unique=True)
