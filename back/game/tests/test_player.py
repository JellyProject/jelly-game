from django.test import TestCase
from authentication.models import User
from profiles.models import Profile

from .. import models
from .. import game_settings as settings


class PlayerTest(TestCase):
    fixtures = ['users', 'source_technologies', 'source_buildings', 'source_events']

    @classmethod
    def setUpTestData(cls):
        new_game = models.Game.create()
        new_game.add_player(Profile.objects.all()[0])

    def setUp(self):
        self.player = models.Player.objects.all()[0]

    def test_score(self):
        self.assertEqual(self.player.score, 50 * 3 + 50 * 2 + 100)
        self.player.balance.economic = 40
        self.player.balance.save()
        player = models.Player.objects.all()[0]
        self.assertEqual(player.score, 40 * 3 + 50 * 2 + 100)
