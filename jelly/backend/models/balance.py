from django.db import models

from .. import game_settings as constant


class Balance(models.Model):
    """
    Balance wheel model

    Fields :
        player (OneToOne -> Player) : Player associated with in a OneToOne link

        economic (int): economic level between 0 and constant.MAX_STATE_VALUE
                            initial value : constant.ECONOMIC_INITIAL_VALUE
        social (int): social level between 0 and constant.MAX_STATE_VALUE
                        initial value : constant.SOCIAL_INITIAL_VALUE
        environmental (int): environment level between 0 and constant.MAX_STATE_VALUE
                        initial value : constant.ENVIRONMENTAL_INITIAL_VALUE
    """
    player = models.OneToOneField('Player', on_delete=models.CASCADE)

    economic = models.IntegerField(default=constant.ECONOMIC_INITIAL_VALUE)
    social = models.IntegerField(default=constant.SOCIAL_INITIAL_VALUE)
    environmental = models.IntegerField(default=constant.ENVIRONMENTAL_INITIAL_VALUE)

    def __str__(self):
        return "Economic, social and environmental balances of " + self.player.profile.user.username

    def green_income(self):
        """ Modify the environment level, according to the environmental level """
        self.environmental += self.environmental // constant.ENVIRONMENTAL_REGENERATION_LEVEL
        self.environmental = min(self.environmental, constant.MAX_STATE_VALUE)
        self.save()
