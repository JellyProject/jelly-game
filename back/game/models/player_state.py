from django.db import models

from .. import game_settings as constant

from .resources import Resources
from .production import Production
from .balance import Balance
from .building import Building
from .technology import Technology
from .source_building import SourceBuilding
from .source_technology import SourceTechnology


class PlayerState(models.Model):
    """
    PlayerState model;

    Fields :
        * balance (OneToOneField <- Balance): player balance
        * resources (OneToOneField <- Resources): resources owned by the player
        * production (OneToOneField <- Production): player production at the beginning of each generation
        * technologies (ForeignKey <- PlayerTechnology): technologies
        * buildings (ForeignKey <- PlayerBuilding): buildings
    """

    _player = models.OneToOneField('Player', null=True, blank=True, related_name='state',
                                   on_delete=models.CASCADE)
    _shadow_player = models.OneToOneField('ShadowPlayer', null=True, blank=True, related_name='state',
                                          on_delete=models.CASCADE)

    def __str__(self):
        return "{0}'s state (Game : {1})".format(self.player.username, self.player.game.pk)

    @property
    def player(self):
        if self._player is not None:
            return self._player
        if self._shadow_player is not None:
            return self._shadow_player
        raise AssertionError("Neither 'player' nor 'shadow_player' is set")

    @classmethod
    def create(cls, new_player):
        """ doc """
        # We test if player is a Player or a ShadowPlayer
        if hasattr(new_player, 'profile'):  # player is a Player (player has a 'profile' field)
            new_state = cls(_player=new_player)
            new_state.save()  # Peut-on faire mieux ?
            new_state._init_state()
        else:  # player is a ShadowPlayer (has no 'profile' field)
            new_state = cls(_shadow_player=new_player)
            new_state.save()  # Peut-on faire mieux ?
            new_state._init_state()

    def _init_state(self):
        """ doc """
        # We create Resources, Production, Balance, Buildings and Technologies associated
        Resources.objects.create(state=self)
        Production.objects.create(state=self)
        Balance.objects.create(state=self)

        for source_building in self.player.game.source_buildings.all():
            unlocked = (source_building.parent_technology is None)
            Building.objects.create(state=self, source=source_building, unlocked=unlocked, quantity_cap=source_building.initial_quantity_cap)

        for source_technology in self.player.game.source_technologies.all():
            unlocked = (source_technology.parent_technology is None)
            Technology.objects.create(state=self, source=source_technology, unlocked=unlocked)

        self.save()

    def has_same_possessions(self, other):
        """ doc """
        if (self.balance != other.balance or
           self.production != other.production or
           self.resources != other.resources):
            return False
        for building in self.buildings.all():
            if building != Building.objects.get(index=building.index, player=other):
                return False
        for technology in self.technologies.all():
            if technology != Technology.objects.get(index=technology.index, player=other):
                return False
        return True

    def purchase_building(self, slug):
        """ Purchase the building with given slug if possible. If not, return an error string. """
        building = self.buildings.get(source__slug=slug)
        (is_purchasable, error_message) = building.is_purchasable()
        if is_purchasable:
            building.copies += 1
            building.trigger_post_purchase_effects()
            building.save()
        return (building, error_message)

    def purchase_technology(self, slug):
        """ Purchase the technology with given slug if possible. If not, return an error string. """
        technology = self.technologies.get(source__slug=slug)
        (is_purchasable, error_message) = technology.is_purchasable()
        if is_purchasable:
            technology.purchased = True
            technology.trigger_post_purchase_effects()
            technology.save()
        return (technology, error_message)
