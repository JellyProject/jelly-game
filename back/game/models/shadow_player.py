from django.db import models

from .. import game_settings as constant

from .virtual_player import VirtualPlayer


class ShadowPlayer(VirtualPlayer):
    """
    Shadow player model, modelize the action pile within each round for a Player

    Inherited fields :
        * balance (OneToOneField <- Balance): player balance
        * resources (OneToOneField <- Resources): resources owned by the player
        * production (OneToOneField <- Production): player production at the beginning of each generation
        * technologies (ForeignKey <- PlayerTechnology): technologies
        * buildings (ForeignKey <- PlayerBuilding): buildings

    New fields :
        * player (OneToOne -> Player)
    """
    player_reference = models.OneToOneField('Player', on_delete=models.CASCADE, editable=False)
