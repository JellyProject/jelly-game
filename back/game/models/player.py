from django.db import models

from .. import game_settings as constant

from .player_resources import Resources
from .player_production import Production
from .player_balance import Balance
# from .user import Profile


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
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name="players")
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="players")

    def __str__(self):
        return self.profile.user.username

    @classmethod
    def create(cls, profile, game):
        """
        Create and return a new Player of profile in game

        Args :
            profile (Profile) : profile which will control this player
            game (Game) : game in which the player will play
        """
        new_player = cls(game=game, profile=profile)
        new_player.save()  # Peut-on faire mieux ?

        Resources.objects.create(player=new_player)
        Production.objects.create(player=new_player)
        Balance.objects.create(player=new_player)

        # Technologies and buildings ??

        new_player.save()
        return new_player

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
