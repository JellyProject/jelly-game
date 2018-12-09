from django.db import models

import game.game_settings as constant
from game.models import Player, Game, Resources, Production, States, HydrocarbonSupplyPile


class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="events")
