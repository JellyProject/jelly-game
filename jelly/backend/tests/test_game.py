from django.test import TestCase
from django.contrib.auth.models import User

from .. import models
from .. import game_settings as constant


class CreateGameTest(TestCase):
    """ Testing the create class method and the _init_supply method """
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def test_create(self):
        """ creation of a game through the create class method which calls _init_supply """
        game = models.Game.create(name="Test game")
        self.assertTrue(models.Game.objects.all()[0].name == "Test game" and len(models.Game.objects.all()) == 1)
        number_of_piles = len(constant.HYDROCARBON_STOCKS_PER_PLAYER)
        for i_pile in range(number_of_piles):
            self.assertEqual(0, game.hydrocarbon_piles.get(index=i_pile).stock_amount)


class GameTest(TestCase):
    """ Testing the create class method and the _init_supply method """
    fixtures = ['sample_data']    # defines a game with one player

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def test_add_player(self):
        """ Test the add_player method """
        user = User.objects.create_user('Luca', 'luca@bongo.cat', 'bongo_cat')
        profile = models.Profile.objects.create(user=user)
        game = models.Game.objects.get(name="game_test")
        number_of_piles = len(constant.HYDROCARBON_STOCKS_PER_PLAYER)
        for i_pile in range(number_of_piles):
            self.assertEqual(constant.HYDROCARBON_STOCKS_PER_PLAYER[i_pile][0],
                             game.hydrocarbon_piles.get(index=i_pile).stock_amount)
        player = game.add_player(profile=profile)
        for i_pile in range(number_of_piles):
            self.assertEqual(constant.HYDROCARBON_STOCKS_PER_PLAYER[i_pile][0] * 2,
                             game.hydrocarbon_piles.get(index=i_pile).stock_amount)
