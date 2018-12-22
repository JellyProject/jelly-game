from django.db import models

from .. import game_settings as constant

from .player_resources import Resources
from .player_production import Production
from .player_balance import States


class Player(models.Model):
    """
    Player model

    Fields :
        game (Game) : ForeignKey link to the game in which the player plays
        user (User) : user which controls the player

        states (OneToOneField <- States): player balance
        resources (OneToOneField <- Resources): resources owned by the player
        production (OneToOneField <- Production): player production at the beginning of each generation
        technologies (ForeignKey <- TechnologyPlayer): technologies
        buildings (ForeignKey <- BuildingPlayer): buildings
    """
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name="players")
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="players")

    def __str__(self):
        return self.user.name

    @classmethod
    def create(cls, user, game):
        """
        Create and return a new Player of user in game

        Arguments :
            user (User) : user which will control this player
            game (Game) : game in which the player will play
        """
        new_player = cls(game=game, user=user)
        new_player.save()  # Peut-on faire mieux ?
        Resources.objects.create(player=new_player)
        Production.objects.create(player=new_player)
        States.objects.create(player=new_player)
        new_player.save()
        return new_player

    def earn_income(self):
        """
        Apply the (beginning of generation) income phase to player

        Adjust money, hydrocarbon, and environment balance
        """
        self.resources.money += self.production.money
        self.states.environmental -= self.production.pollution
        self.green_income()
        # Cas des hydrocarbures
        hydrocarbon_stock = self.game.hydrocarbon_piles.get(index=self.game.current_index_pile)
        self.resources.hydrocarbons += self.production.hydrocarbons * hydrocarbon_stock.multiplier
        hydrocarbon_stock.decrease(self.production.hydrocarbons * hydrocarbon_stock.multiplier)

        self.resources.save()
        self.states.save()

    def green_income(self):
        """ Apply the environment generation income to the environment balance """
        self.states.green_income()
