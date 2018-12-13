from django.db import models

from .. import game_settings as constant


class Player(models.Model):
    """
    Player model

    Fields:
        name (CharField): name of the player country
        resources (OneToOneField): Resources possessed by the player
        production (OneToOneField): player Production
        states (OneToOneField): player States
        technologies (OneToOneField?): technologies (not implemented yet)
        built (OneToOneField?): building built (not implemented yet)
    """
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name="players")
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="players")

    def __str__(self):
        return self.user.name

    def new(self, user, game):
        new_player = Player.objects.create(game=self, user=user)
        Resources.objects.create(player=new_player)
        Production.objects.create(player=new_player)
        States.objects.create(player=new_player)

    def earn_income(self):
        """
        Gain des revenus : money, hydrocarbures, pollution, et regeneration de l'envirronement
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
        self.states.green_income()
