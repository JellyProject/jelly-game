from django.db import models

from .. import game_settings as constant


class SourceEvent(models.Model):
    """
    Source event model.

    Fields :
        * name (char) : A unique human-readable name.
        * slug (char) : A simple and unique string to identify self.
        * version (char) : The game version self belongs to.
        * era (char) : The era self belongs to.
        * description (text) : A human-readable description of self.
        * is_final (bool) : Tell it is a final event 
    """
    effect_events = {
        "mouvements-sociaux": "mouvements_sociaux"
    }

    name = models.CharField(max_length=40, default='Sunny day', editable=False)
    slug = models.CharField(max_length=40, default='sunny-day', editable=False)
    version = models.CharField(max_length=20, default='jelly', editable=False)
    era = models.IntegerField(default=1, editable=False)
    description = models.TextField(default='There is nothing to report.', editable=False)
    is_final = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return "{0} (Version : {1})".format(self.name, self.version)

    def execute_effect(self, game):
        '''
            Call a callback function for buildings with a special effect
        '''
        method_prefix = self.effect_events.get(self.slug, "no_special_effect")
        if method_prefix != "no_special_effect":
            exec("self." + method_prefix + "_effect(game)")

    def mouvements_sociaux_effect(self, game):
        if self.version == 'jelly':
            for player in game.players.all():
                social_balance = player.balance.social
                if social_balance <= 30:
                    player.balance.economic -= 20
                elif social_balance <= 50:
                    player.balance.economic -= 10
                player.balance.save()
