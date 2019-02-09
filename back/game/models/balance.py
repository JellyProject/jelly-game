from django.db import models

from .. import game_settings as constant


class Balance(models.Model):
    """
    Balance wheel model

    Fields :
        * state (OneToOne -> PlayerState) : global state of the player related to the balance

        * economic (int): economic level between 0 and constant.MAX_STATE_VALUE
                            initial value : constant.ECONOMIC_INITIAL_VALUE
        * social (int): social level between 0 and constant.MAX_STATE_VALUE
                        initial value : constant.SOCIAL_INITIAL_VALUE
        * environmental (int): environment level between 0 and constant.MAX_STATE_VALUE
                        initial value : constant.ENVIRONMENTAL_INITIAL_VALUE
    """
    state = models.OneToOneField('PlayerState', on_delete=models.CASCADE, related_name='balance', editable=False)

    economic = models.IntegerField(default=constant.ECONOMIC_INITIAL_VALUE)
    social = models.IntegerField(default=constant.SOCIAL_INITIAL_VALUE)
    environmental = models.IntegerField(default=constant.ENVIRONMENTAL_INITIAL_VALUE)

    def __str__(self):
        return "Balance (Game : {0}, Player : {1})".format(self.player.game.pk, self.player.username())

    def __eq__(self, other):
        return (self.player.id == other.player.id and
                self.economic == other.economic and
                self.social == other.social and
                self.environmental == other.environmental)

    @property
    def player(self):
        return self.state.player

    def green_income(self):
        """ Modify the environment level, according to the environmental level """
        self.environmental += self.environmental // constant.ENVIRONMENTAL_REGENERATION_LEVEL
        self.environmental = min(self.environmental, constant.MAX_STATE_VALUE)
        self.save()
