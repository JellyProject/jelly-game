from django.test import TestCase
from authentication.models import User
from profiles.models import Profile

from .. import models
from .. import game_settings as settings


class PlayerTest(TestCase):
    """ Testing the create class method and the _init_supply method """
    fixtures = ['users', 'source_technologies', 'source_buildings', 'source_events']

    @classmethod
    def setUpTestData(cls):
        new_game = models.Game.create()
        new_game.add_player(Profile.objects.all()[0])

    def setUp(self):
        self.player = models.Player.objects.all()[0]
        pass

    def test_player_creation(self):
        """ doc """
        self.assertTrue(self.player.state.has_same_possessions(self.player.shadow.state))

    def test_shadow_player_modification(self):
        """ doc """
        self.player.shadow.state.balance.economic += 1
        self.player.shadow.state.balance.save()

        player = models.Player.objects.all()[0]
        self.assertFalse(player.state.has_same_possessions(player.shadow.state))

        building = self.player.shadow.state.buildings.get(source__slug='usine-avancee')
        building.unlocked = True
        building.save()

        player = models.Player.objects.all()[0]
        self.assertTrue(player.shadow.state.buildings.get(source__slug='usine-avancee').unlocked)

        self.player.update()
        player = models.Player.objects.all()[0]
        self.assertTrue(player.state.has_same_possessions(player.shadow.state))

    def test_player_modification(self):
        pass
