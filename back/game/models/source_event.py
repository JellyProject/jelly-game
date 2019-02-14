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
        "mouvements-sociaux": "mouvements_sociaux",
        "maree-noire": "maree_noire",
        "crise-economique": "crise_economique",
        "crise-mondiale": "crise_mondiale",
        "nouveau-gisement": "nouveau_gisement",
        "tensions-internationales": "tensions_internationales",
        "decouverte-du-radium": "decouverte_du_radium",
        "guerre-mondiale": "guerre_mondiale",
        "les-trente-glorieuses": "les_trente_glorieuses"
    }

    name = models.CharField(max_length=40, default='Sunny day', editable=False)
    slug = models.CharField(max_length=40, default='sunny-day', editable=False)
    version = models.CharField(max_length=20, default='jelly', editable=False)
    era = models.IntegerField(default=1, editable=False)
    description = models.TextField(default='There is nothing to report.', editable=False)
    is_final = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return "{0} (Version : {1})".format(self.name, self.is_final)

    def execute_effect(self, game):
        '''
            Call a callback function for buildings with a special effect
        '''
        method_prefix = self.effect_events.get(self.slug, "no_special_effect")
        if method_prefix != "no_special_effect":
            exec("self." + method_prefix + "_effect(game)")

    def mouvements_sociaux_effect(self, game):
        """
        Evènement social individuel
            * -10 en économie si <= 50
            * -20 en économie si <= 30
        """
        if self.version == 'jelly':
            for player in game.players.all():
                social_balance = player.balance.social
                if social_balance <= 30:
                    player.balance.economic -= 20
                elif social_balance <= 50:
                    player.balance.economic -= 10
                player.balance.save()

    def maree_noire_effect(self, game):
        """ Le joueur possédant le plus d'hydrocarbures gagne 5 pollution """
        if self.version == 'jelly':
            player_max_hydrocarbon = 0
            max_stock = 0
            for player in len(game.players.all()):
                hydrocarbon_resources = player.resources.hydrocarbon
                if hydrocarbon_resources >= max_stock:
                    player_max_hydrocarbon = player
                    max_stock = hydrocarbon_resources

            player.resources.pollution += 10
            player.resources.save()

    def crise_economique_effect(self, game):
        """
        Evènement économique individuel
            * -10 en social si <= 50
            * -20 en social si <= 30
        """
        if self.version == 'jelly':
            for player in game.players.all():
                economic_balance = player.balance.economic
                if economic_balance <= 30:
                    player.balance.social -= 20
                elif economic_balance <= 50:
                    player.balance.social -= 10
                player.balance.save()

    def crise_mondiale_effect(self, game):
        """
        Evènement économique moyenné
            * -10 en social si <= 50
            * -20 en social si <= 30
        """
        if self.version == 'jelly':
            mean = 0
            for player in game.players.all():
                economic_balance = player.balance.economic
                mean += economic_balance
            mean /= len(game.players.all())
            for player in game.players.all():
                if mean <= 30:
                    player.balance.social -= 20
                elif mean <= 50:
                    player.balance.social -= 10
                player.balance.save()

    def nouveau_gisement_effect(self, game):
        """
        Rien pour l'instant
        """
        pass

    # def tensions_internationales_effect(self, game): # A ajouter plus tard 

    def boom_demographique_effect(self, game):
        """
        -1 de production nourriture pour chaque joueur
        """
        if self.version == "jelly":
            for player in game.players.all():
                player.production.food -= 1
                player.production.save()

    def decouverte_du_radium(self, game):
        """ Chaque joueur gagne 1 point de production d'électricité """
        if self.version == "jelly":
            for player in game.players.all():
                player.production.electricity += 1
                player.production.save()

    def guerre_mondiale(self, game):
        """
        Evènement social moyenné
            * -10 en économie si <= 100
            * -10 en économie et en social si <= 50
            * -10 en économie et -20 en social si <= 40

        +1 de production de nourriture pour chaque joueur
        """
        if self.version == "jelly":
            for player in game.players.all():
                # first effet
                player.production.food += 1
                player.production.save()
                # second effect
                social_balance = player.balance.social
                if social_balance <= 40:
                    player.balance.economic -= 10
                    player.balance.social -= 20
                elif social_balance <= 50:
                    player.balance.economic -= 10
                    player.balance.social -= 10
                elif social_balance <= 100:
                    player.balance.economic -= 10
                player.balance.save()

    def les_trente_glorieuses(self, game):
        """ Chaque joueur gagne 10 point d'économie """
        if self.version == "jelly":
            for player in game.players.all():
                player.balance.economic += 10
                player.balance.save()
