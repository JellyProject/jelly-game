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
        "les-trente-glorieuses": "les_trente_glorieuses",
        "nouveau-gisement": "nouveau_gisement",
        "fuites-de-décharges": "fuites_de_decharges",
        "dechets-nucleaires": "dechets_nucleaires",
        "maree-noire": "maree_noire",
        "boom-demographique": "boom_demographique",
        "tensions-internationales": "tensions_internationales",
        "aide-internationale": "aide_internationale",
        "mouvements-sociaux": "mouvements_sociaux",
        "secheresse": "secheresse",
        "pollution-des-sols": "pollution_des_sols",
        "boom-economique": "boom_economique",
        "mondialisation": "mondialisation",
        "reestimation-des-stocks": "reestimation_des_stocks",
        "black-out": "black_out",
        "explosion-de-depots-petroliers": "explosion_de_depots_petroliers",
        "elections-presidentielles": "elections_presidentielles",
        "desertification": "desertification",
        "pollution-de-l-air": "pollution_de_l_air",
        "canicule": "canicule",
        "crise-economique": "crise_economique",
        "crise-mondiale": "crise_mondiale",
        "dernier-tour": "dernier_tour"
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
        +2 hydrocarbures par joueur dans la pile courante
        """
        if self.version == "jelly":
            current_pile = game.hydrocarbon_piles.get(index=game.current_index_pile)
            current_pile.stock_amount += 2 * len(game.players.all())
            current_pile.save()

    # def tensions_internationales_effect(self, game): # A ajouter plus tard quand il y aura les importations

    def boom_demographique_effect(self, game):
        """
        -1 de production nourriture pour chaque joueur
        """
        if self.version == "jelly":
            for player in game.players.all():
                player.production.food -= 1
                player.production.save()

    def decouverte_du_radium(self, game):
        """
        Chaque joueur gagne 1 point de production d'électricité

        Passage à l'ère 2
        """
        if self.version == "jelly":
            for player in game.players.all():
                player.production.electricity += 1
                player.production.save()

        game.era = 2
        game.save()

    def guerre_mondiale(self, game):
        """
        Evènement social moyenné
            * -10 en économie si <= 100
            * -10 en économie et en social si <= 50
            * -10 en économie et -20 en social si <= 40

        +1 de production de nourriture pour chaque joueur

        Passage à l'ère 2
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

        game.era = 2
        game.save()

    def les_trente_glorieuses(self, game):
        """
        Chaque joueur gagne 10 point d'économie

        Passage à l'ère 2
        """
        if self.version == "jelly":
            for player in game.players.all():
                player.balance.economic += 10
                player.balance.save()

        game.era = 2
        game.save()

    def nouveau_gisement_effect(self, game):
        """
        doc
        """
        pass

    def fuites_de_decharges_effect(self, game):
        """
        doc
        """
        pass

    def dechets_nucleaires_effect(self, game):
        """
        doc
        """
        pass

    def maree_noire_effect(self, game):
        """
        doc
        """
        pass

    def boom_demographique_effect(self, game):
        """
        doc
        """
        pass

    # def tensions_internationales_effect(self, game): # A ajouter plus tard quand il y aura les importations

    def aide_internationale_effect(self, game):
        """
        doc
        """
        pass

    def mouvements_sociaux_bis_effect(self, game):
        """
        doc
        """
        pass

    def secheresse_effect(self, game):
        """
        doc
        """
        pass

    def pollution_des_sols_effect(self, game):
        """
        doc
        """
        pass

    def boom_economique_effect(self, game):
        """
        doc
        """
        pass

    def mondialisation_effect(self, game):
        """
        doc
        """
        pass

    def reestimation_des_stocks_effect(self, game):
        """
        doc
        """
        pass

    def black_out_effect(self, game):
        """
        doc
        """
        pass

    def explosion_de_depots_petroliers_effect(self, game):
        """
        doc
        """
        pass

    def elections_presidentielle_effect(self, game):
        """
        doc
        """
        pass
