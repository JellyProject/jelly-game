from django.test import TestCase
from django.contrib.auth.models import User

from .. import models
from .. import game_settings as settings


class EventTest(TestCase):
    """ doc """
    fixtures = ['users', 'source_events']

    @classmethod
    def setUpTestData(cls):
        game = models.Game.create()
        john = models.Profile.objects.all()[0]
        game.add_player(john)

    def setUp(self):
        pass

    def test_event_effect(self):
        game = models.Game.objects.all()[0]
        john = models.Profile.objects.all()[0]
        event = models.SourceEvent.objects.get(slug='mouvements-sociaux')
        event.execute_effect(game)
        self.assertEqual(john.players.all()[0].balance.economic, 40)
