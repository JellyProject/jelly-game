from django.test import TestCase
from django.contrib.auth.models import User

from .. import models
from .. import game_settings as settings


class GameTest(TestCase):
    """ Testing the create class method and the _init_supply method """
    fixtures = ['users', 'source_technologies', 'source_buildings']

    @classmethod
    def setUpTestData(cls):
        models.Game.create()

    def setUp(self):
        pass

    def test_game_creation(self):
        """ Test the create class method from Game model. """
        self.assertTrue(len(models.Game.objects.all()) == 1)
        game = models.Game.objects.all()[0]

        # Hydrocarbon piles initialization test
        number_of_piles = len(settings.HYDROCARBON_STOCKS_PER_PLAYER)
        for i_pile in range(number_of_piles):
            self.assertEqual(0, game.hydrocarbon_piles.get(index=i_pile).stock_amount)

        # Events initialization test [TO DO]

        # Source buildings loading test
        version_source_buildings = models.SourceBuilding.objects.filter(version=game.version)
        self.assertEqual(version_source_buildings.count(), game.source_buildings.count())
        for version_source_building in version_source_buildings:
            self.assertEqual(version_source_building, game.source_buildings.get(slug=version_source_building.slug))

        # Source events loading test [TO DO]

        # Source technologies loading test
        version_source_technologies = models.SourceTechnology.objects.filter(version=game.version)
        self.assertEqual(version_source_technologies.count(), game.source_technologies.count())
        for version_source_technology in version_source_technologies:
            self.assertEqual(version_source_technology,
                             game.source_technologies.get(slug=version_source_technology.slug))

    def test_add_player(self):
        """ Test the add_player method """
        user = User.objects.create_user('Luca', 'luca@bongo.cat', 'bongo_cat')
        profile = models.Profile.objects.get(user=user)
        game = models.Game.objects.all()[0]
        number_of_piles = len(settings.HYDROCARBON_STOCKS_PER_PLAYER)
        for i_pile in range(number_of_piles):
            self.assertEqual(game.hydrocarbon_piles.get(index=i_pile).stock_amount, 0)
        game.add_player(profile=profile)
        for i_pile in range(number_of_piles):
            self.assertEqual(game.hydrocarbon_piles.get(index=i_pile).stock_amount,
                             settings.HYDROCARBON_STOCKS_PER_PLAYER[i_pile][0])
