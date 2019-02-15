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
        "boom-demographique": "boom_demographique",
        "decouverte-du-radium": "decouverte_du_radium",
        "guerre-mondiale": "guerre_mondiale",
        "les-trente-glorieuses": "les_trente_glorieuses",
        "nouveau-gisement-bis": "nouveau_gisement",
        "fuites-de-décharges": "fuites_de_decharges",
        "dechets-nucleaires": "dechets_nucleaires",
        "maree-noire-bis": "maree_noire_bis",
        "boom-demographique-bis": "boom_demographique_bis",
        "tensions-internationales": "tensions_internationales",
        "aide-internationale": "aide_internationale",
        "mouvements-sociaux-bis": "mouvements_sociaux_bis",
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
        "crise-economique-bis": "crise_economique_bis",
        "crise-mondiale-bis": "crise_mondiale_bis",
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
            for player in game.players.all():
                hydrocarbon_resources = player.resources.hydrocarbon
                if hydrocarbon_resources >= max_stock:
                    player_max_hydrocarbon = player
                    max_stock = hydrocarbon_resources
            player.resources.pollution += 5
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
            current_pile.stock_amount += 2 * game.players.count()
            current_pile.save()

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

    def nouveau_gisement_bis_effect(self, game):
        """
        +3 hydrocarbures par joueur dans la pile courante
        """
        if self.version == "jelly":
            current_pile = game.hydrocarbon_piles.get(index=game.current_index_pile)
            current_pile.stock_amount += 3 * game.players.count()
            current_pile.save()

    def fuites_de_decharges_effect(self, game):
        """
        Rien pour l'instant
        """
        pass

    def dechets_nucleaires_effect(self, game):
        """
        -10 environmental pour chaque joueur possédant une centrale nucléaire
        """
        if self.version == "jelly":
            for player in game.players.all():
                if len(player.buildings.filter(slug="centrale-nucleaire")) != 0:
                    player.balance.environmental -= 10

    def maree_noire_bis_effect(self, game):
        """ Le joueur possédant le plus d'hydrocarbures gagne 5 pollution """
        self.maree_noire_effect(game)

    def boom_demographique_bis_effect(self, game):
        """
        Evènement économique individuel
            * -3 de nourriture si <= 30
            * -2 de nourriture si <= 50
            * -1 de nourriture si <= 70
        """
        if self.version == "jelly":
            for player in game.players.all():
                if player.balance.economic <= 30:
                    player.production.food -= 3
                elif player.balance.economic <= 50:
                    player.production.food -= 2
                elif player.balance.economic <= 70:
                    player.production.food -= 1
                player.production.save()

    def tensions_internationales_effect(self, game):  # A ajouter plus tard quand il y aura les importations
        pass

    def aide_internationale_effect(self, game):
        """
        Evènement économique individuel, -5 social si affecté
            * +12 UM si <= 20
            * +9 UM si <= 30
            * +6 UM si <= 40
        """
        if self.version == "jelly":
            for player in game.players.all():
                # If the player is affected by the event
                if player.balance.economic <= 40:
                    player.balance.social -= 5
                    player.balance.save()
                # else, we skip to the next player
                else:
                    continue

                if player.balance.economic <= 20:
                    player.resources.monye += 12
                elif player.balance.economic <= 30:
                    player.resources.monye += 9
                elif player.balance.economic <= 40:
                    player.resources.monye += 6
                player.balance.save()

    def mouvements_sociaux_bis_effect(self, game):
        """
        Evènement social individuel
            * -5 en économie si <= 70
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
                elif social_balance <= 70:
                    player.balance.economic -= 5
                player.balance.save()

    def secheresse_effect(self, game):
        """
        Evènement environemental moyenné
            * -1 de nourriture si <= 40
            * -2 en social si <= 30
            * -3 en social si <= 20
        """
        if self.version == 'jelly':
            mean = 0
            for player in game.players.all():
                environmental_balance = player.balance.environmental
                mean += environmental_balance
            mean /= game.players.count()
            for player in game.players.all():
                if mean <= 20:
                    player.production.food -= 3
                elif mean <= 30:
                    player.production.food -= 2
                elif mean <= 40:
                    player.production.food -= 1
                player.production.save()

    def pollution_des_sols_effect(self, game):
        """
        Evènement environemental individuel
            * -1 de nourriture si <= 40
            * -2 de nourriture si <= 30
            * -3 de nourriture si <= 20
        """
        if self.version == 'jelly':
            for player in game.players.all():
                if player.balance.environmental <= 20:
                    player.production.food -= 3
                elif player.balance.environmental <= 30:
                    player.production.food -= 2
                elif player.balance.environmental <= 40:
                    player.production.food -= 1
                player.production.save()

    def boom_economique_effect(self, game):
        """
        Evènement économique individuel
            * +10 en économie si <= 50
            * +10 en économie si <= 30
        """
        if self.version == 'jelly':
            for player in game.players.all():
                if player.balance.economic <= 30:
                    player.balance.economic += 10
                    player.resources.money += 1
                elif player.balance.economic <= 50:
                    player.balance.economic += 10
                player.balance.save()
                player.resources.save()

    def mondialisation_effect(self, game):
        """
        Evènement économique individuel
            * -10 en économie si <= 30
            * +10 en économie si >= 70
        """
        if self.version == 'jelly':
            for player in game.players.all():
                if player.balance.economic <= 30:
                    player.balance.economic += 10
                elif player.balance.economic >= 70:
                    player.balance.economic -= 10
                player.balance.save()

    def reestimation_des_stocks_effect(self, game):
        """
        Rien pour l'instant
        """
        pass

    def black_out_effect(self, game):
        """
        -1 UM pour chaque consommation d'électricité
        """
        if self.version == 'jelly':
            for player in game.players.all():
                if player.production.electricity < 0:
                    player.resources.money += player.production.electricity
                    player.resources.save()

    def explosion_de_depots_petroliers_effect(self, game):
        """
        -50% sur les reserves d'hydrocarbures de chaque joueur
        """
        if self.version == 'jelly':
            for player in game.players.all():
                player.resources.hydrocarbon = player.resources.hydrocarbon // 2
                player.resources.save()

    def elections_presidentielle_effect(self, game):
        """
        Evènement social individuel
            * +10 économie si >= 80
            * -10 économie si <= 40
        """
        if self.version == 'jelly':
            for player in game.players.all():
                if player.balance.social <= 40:
                    player.balance.economic -= 10
                elif player.balance.social >= 80:
                    player.balance.economic += 10
                player.balance.save()

    def desertification_effect(self, game):
        """
        Evènement environemental individuel
            * -10 en social si <= 50
            * -20 en social si <= 30
        """
        if self.version == 'jelly':
            for player in game.players.all():
                if player.balance.environmental <= 30:
                    player.balance.social -= 20
                elif player.balance.environmental <= 50:
                    player.balance.social -= 10
                player.balance.save()

    def pollution_de_l_air_effect(self, game):
        """
        Evènement environemental individuel
            * -10 en économie si <= 70
            * -10 en économie et -10 en social si <= 50
            * -20 en économie et -10 en social en social si <= 30
        """
        if self.version == 'jelly':
            for player in game.players.all():
                if player.balance.environmental <= 30:
                    player.balance.social -= 10
                    player.balance.economic -= 20
                elif player.balance.environmental <= 50:
                    player.balance.social -= 10
                    player.balance.economic -= 10
                elif player.balance.environmental <= 70:
                    player.balance.economic -= 10
                player.balance.save()

    def canicule_effect(self, game):
        """
        Evènement environemental individuel
            * -10 en économie si <= 70
            * -10 en économie et -10 en social si <= 50
            * -20 en économie et -10 en social en social si <= 30
        """
        if self.version == 'jelly':
            for player in game.players.all():
                if player.balance.environmental <= 40:
                    player.resources.money -= 9
                elif player.balance.environmental <= 60:
                    player.resources.money -= 6
                elif player.balance.environmental <= 80:
                    player.resources.money -= 3
                player.resources.save()

    def crise_economique_bis_effect(self, game):
        """
        Evènement économique individuel
            * -10 en social si <= 50
            * -20 en social si <= 30
        """
        self.crise_economique_effect(game)

    def crise_mondiale_bis_effect(self, game):
        """
        Evènement économique moyenné
            * -10 en social si <= 50
            * -20 en social si <= 30
        """
        self.crise_mondiale_effect(game)

    def dernier_tour_effect(self, game):
        """
        Déclenche le dernier tour
        """
        pass
