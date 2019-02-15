from django.test import TestCase
from django.contrib.auth.models import User

from .. import models
from profiles.models import Profile
from .. import game_settings as settings


class EventTest(TestCase):
    """ Testing events """
    fixtures = ['users', 'source_events']

    @classmethod
    def setUpTestData(cls):
        game = models.Game.create()
        john = Profile.objects.all()[0]
        game.add_player(john)

    def setUp(self):
        pass

    def test_event_effect(self):
        """ Testing the implementation of event effects """
        game = models.Game.objects.all()[0]
        john = Profile.objects.all()[0]
        event = models.SourceEvent.objects.get(slug='mouvements-sociaux', era=1)
        event.execute_effect(game)
        self.assertEqual(john.players.all()[0].balance.economic, 40)
