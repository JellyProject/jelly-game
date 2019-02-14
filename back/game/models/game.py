from django.db import models

from .. import game_settings as constant

from .player import Player
from .hydrocarbon_supply_pile import HydrocarbonSupplyPile
from .source_building import SourceBuilding
from .source_event import SourceEvent
from .source_technology import SourceTechnology
from .event import Event

import random


class Game(models.Model):
    """
    Game model, representing a "world"

    Fields :
        * name (string) : name of the game
        * current_index_pile (int) : index of the current hydrocarbon pile in which players take ressources
        * source_events (ManyToMany -> SourceEvent):
        * source_buildings (ManyToMany -> SourceBuilding):
        * source_technologies (ManyToMany -> SourceTechnology):

        * players (ForeignKey <- Player) : query set of players in the game
        * hydrocarbon_piles (ForeignKey <- HydrocarbonSupplyPile) : query set of hydrocarbon supply piles in the game
    """

    version = models.CharField(max_length=20, default='jelly', editable=False)  # Game version
    creation_date = models.DateTimeField(auto_now_add=True)
    last_save_date = models.DateTimeField(auto_now=True)
    turn = models.IntegerField(default=1)
    era = models.IntegerField(default=1)
    current_index_pile = models.IntegerField(default=0)
    source_buildings = models.ManyToManyField('SourceBuilding')
    source_events = models.ManyToManyField('SourceEvent')
    source_technologies = models.ManyToManyField('SourceTechnology')

    def __str__(self):
        text = "{0} (Players : ".format(self.pk)
        for player in self.players.all():
            text += player.username() + ", "
        return text[:-2] + ")"

    @classmethod
    def create(cls, version="jelly"):
        """
        Create a new Game

        Args :
            version (string) : version of the new game
        """
        game = cls(version=version)
        game.save()
        game._init_source_buildings()
        game._init_source_technologies()
        game._init_source_events()
        game._create_event_deck()
        game._init_supply()
        return game

    def _init_source_buildings(self):
        """ Links the game to its version source buildings. """
        version_source_buildings = SourceBuilding.objects.filter(version=self.version)
        for version_source_building in version_source_buildings:
            self.source_buildings.add(version_source_building)

    def _init_source_technologies(self):
        """ Links the game to its version source technologies. """
        version_source_technologies = SourceTechnology.objects.filter(version=self.version)
        for version_source_technology in version_source_technologies:
            self.source_technologies.add(version_source_technology)

    def _init_source_events(self):
        """ Links the game to its version source events. """
        version_source_events = SourceEvent.objects.filter(version=self.version)
        for version_source_event in version_source_events:
            self.source_events.add(version_source_event)

    def _init_supply(self):
        """ Initialize the hydrocarbon supply piles. """
        const = constant.HYDROCARBON_STOCKS_PER_PLAYER
        for pile_index in range(len(const)):
            HydrocarbonSupplyPile.objects.create(stock_amount=0,
                                                 multiplier=const[pile_index][1],
                                                 index=pile_index,
                                                 game=self)

    def _create_event_deck_for_era(self, era):
        """ Create the event deck for the era era """
        era_source_events = list(SourceEvent.objects.filter(era=era))
        deck_size = 0
        # First part
        while deck_size < constant.EVENT_DECK_MIN_SIZE['era' + str(era)] - 1:
            rand_event = era_source_events[random.randint(0, len(era_source_events) - 1)]
            if rand_event.is_final:
                continue
            # else
            deck_size += 1
            Event.objects.create(source=rand_event, game=self, index=len(Event.objects.all()))
            era_source_events.remove(rand_event)
        # Second part
        while deck_size < constant.EVENT_DECK_MAX_SIZE['era' + str(era)]:
            rand_event = era_source_events[random.randint(0, len(era_source_events) - 1)]
            # If the last event is not final
            if (not rand_event.is_final) and (deck_size == constant.EVENT_DECK_MAX_SIZE['era' + str(era)] - 1):
                continue
            deck_size += 1
            Event.objects.create(source=rand_event, game=self, index=deck_size)
            # If we chose a final event, the era event deck is complete
            if rand_event.is_final:
                break
            # else
            era_source_events.remove(rand_event)

    def _create_event_deck(self):
        """ Event deck creation for all eras """
        for era in range(1, constant.NUMBER_OF_ERAS + 1):
            self._create_event_deck_for_era(era)

    def add_player(self, profile):
        """
        Adds a player in the game and updates the global hydrocarbon supplies accordingly

        Args :
            profile (Profile) : profile controlling the new player
        """
        # Check if a player already has this profile
        if not Player.objects.filter(game=self, profile=profile):
            # new_player = Player.objects.create(game=self, user=user)
            # Resources.objects.create(player=new_player)
            # Production.objects.create(player=new_player)
            # Balance.objects.create(player=new_player)
            new_player = Player.create(profile=profile, game=self)
            # ajustement du stock mondial d'hydrocarbures
            const = constant.HYDROCARBON_STOCKS_PER_PLAYER
            for pile_index in range(len(const)):
                self.hydrocarbon_piles.get(index=pile_index).decrease(-const[pile_index][0])
        else:    # For debugging purposes, should be deleted or modified
            print("A player already has this user name, please choose another one.")    # Print in console

    def update_index_pile(self):
        """ Update the index of the current hydrocarbon supply pile """
        # if there is no more hydrocarbon in the current pile, change pile (while in case of problems)
        hydrocarbon_piles = self.hydrocarbon_piles.order_by('index')
        while hydrocarbon_piles[self.current_index_pile].is_empty():
            self.current_index_pile += 1
            overflow = -hydrocarbon_piles[self.current_index_pile - 1].stock_amount
            hydrocarbon_piles[self.current_index_pile].decrease(overflow)
            hydrocarbon_piles[self.current_index_pile - 1].set_to(0)
        self.save()

    def income_phase(self):
        """ Run income phase for each player"""
        # income for each player
        for player in self.players.all():
            player.earn_income()
        # update of the current pile index
        self.update_index_pile()

    def main_phase(self):
        """ Main phase """
        pass

    def event_phase(self):
        pass
