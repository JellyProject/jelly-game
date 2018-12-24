from django.test import TestCase

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
    @classmethod
    def setUpTestData(cls):
        game = models.Game.create(name="Test game")

    def setUp(self):
        pass

    def test_add_player(self):
        """ Test the add_player method """
        user = models.User.objects.create(name="Miguel", )
        player = models.Game.objects.get(name="Test game").add_player(user=user)
        game = models.Game.objects.get(name="Test game")
        game.hydrocarbon_piles
        number_of_piles = len(constant.HYDROCARBON_STOCKS_PER_PLAYER)
        for i_pile in range(number_of_piles):
            self.assertEqual(constant.HYDROCARBON_STOCKS_PER_PLAYER[i_pile][0], game.hydrocarbon_piles.get(index=i_pile).stock_amount)
