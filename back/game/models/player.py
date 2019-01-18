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
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="players", editable=False)

    def __str__(self):
        return "{0} (Game : {1})".format(self.username(), self.game.name)

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
        #source_building = models.SourceBuilding.objects.all()[0]
        new_player = cls(game=game, profile=profile)
        new_player.save()  # Peut-on faire mieux ?

        Resources.objects.create(player=new_player)
        Production.objects.create(player=new_player)
        Balance.objects.create(player=new_player)

        nb_source_buildings = SourceBuilding.objects.all().count()
        for i in range(1, nb_source_buildings + 1):    # index starts at 1
            source_building = SourceBuilding.objects.get(pk=i)
            unlocked = source_building.parent_technology == None
            Building.objects.create(player=new_player, index=i, unlocked=unlocked)

        nb_source_technologies = SourceTechnology.objects.all().count()
        for i in range(1, nb_source_technologies + 1):    # index starts at 1
            source_technology = SourceTechnology.objects.get(pk=i)
            unlocked = source_technology.parent_technology == None
            Technology.objects.create(player=new_player, index=i, unlocked=unlocked)

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

    def purchase_building(self, id):
        """ Purchase the building with index id if possible. If not, returns an error string. """
        building = self.buildings.get(index=id)
        (is_purchasable, error_message) = building.is_purchasable()
        if is_purchasable:
            building.purchase()
        return (building, error_message)

    def purchase_technology(self, id):
        """ Purchase the technology with index id if possible. If not, returns an error string. """
        technology = self.technologies.get(index=id)
        (is_purchasable, error_message) = technology.is_purchasable()
        if is_purchasable:
            technology.purchase()
        return (technology, error_message)