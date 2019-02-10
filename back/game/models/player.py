from django.db import models

from .. import game_settings as constant

from .resources import Resources
from .production import Production
from .balance import Balance
from .building import Building
from .technology import Technology
from .source_building import SourceBuilding
from .source_technology import SourceTechnology


class Player(models.Model):
    """
    Player model

    Fields :
        game (Game) : ForeignKey link to the game in which the player plays
        profile (Profile) : profile which controls the player

        balance (OneToOneField <- Balance): player balance
        resources (OneToOneField <- Resources): resources owned by the player
        production (OneToOneField <- Production): player production at the beginning of each generation
        technologies (ForeignKey <- PlayerTechnology): technologies
        buildings (ForeignKey <- PlayerBuilding): buildings
    """
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name="players", editable=False)
    profile = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name="players", editable=False)

    def __str__(self):
        return "{0} (Game : {1})".format(self.username(), self.game.pk)

    def __eq__(self, other):
        return (self.game.id == other.game.id and
                self.profile.id == other.profile.id)

    def has_same_possessions(self, other):
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

    @classmethod
    def create(cls, profile, game):
        """
        Create and return a new Player of profile in game

        Args :
            profile (Profile) : profile which will control this player
            game (Game) : game in which the player will play
        """
        # source_building = models.SourceBuilding.objects.all()[0]
        new_player = cls(game=game, profile=profile)
        new_player.save()  # Peut-on faire mieux ?

        Resources.objects.create(player=new_player)
        Production.objects.create(player=new_player)
        Balance.objects.create(player=new_player)

        for source_building in game.source_buildings.all():
            unlocked = (source_building.parent_technology is None)
            Building.objects.create(player=new_player, slug=source_building.slug, unlocked=unlocked)

        for source_technology in game.source_technologies.all():
            unlocked = (source_technology.parent_technology is None)
            Technology.objects.create(player=new_player, slug=source_technology.slug, unlocked=unlocked)

        new_player.save()
        return new_player

    def username(self):
        """ Return the username of this player. """
        return self.profile.user.username

    def earn_income(self):
        """
        Apply the (beginning of generation) income phase to player

        Adjust money, hydrocarbon, and environment balance
        """
        self.resources.money += self.production.money
        self.balance.environmental -= self.production.pollution
        self.green_income()
        # Cas des hydrocarbures
        hydrocarbon_stock = self.game.hydrocarbon_piles.get(index=self.game.current_index_pile)
        self.resources.hydrocarbon += self.production.hydrocarbon * hydrocarbon_stock.multiplier
        hydrocarbon_stock.decrease(self.production.hydrocarbon * hydrocarbon_stock.multiplier)

        self.resources.save()
        self.balance.save()

    def green_income(self):
        """ Apply the environment generation income to the environment balance """
        self.balance.green_income()

    def purchase_building(self, slug):
        """ Purchase the building with given slug if possible. If not, return an error string. """
        building = self.buildings.get(slug=slug)
        (is_purchasable, error_message) = building.is_purchasable()
        if is_purchasable:
            building.copies += 1
            building.trigger_post_purchase_effects()
            building.save()
        return (building, error_message)

    def purchase_technology(self, slug):
        """ Purchase the technology with given slug if possible. If not, return an error string. """
        technology = self.technologies.get(slug=slug)
        (is_purchasable, error_message) = technology.is_purchasable()
        if is_purchasable:
            technology.purchased = True
            technology.trigger_post_purchase_effects()
            technology.save()
        return (technology, error_message)
