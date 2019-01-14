from django.test import TestCase

from .. import models


class PlayerTest(TestCase):
    """ doc """
    @classmethod
    def setUpTestData(cls):
        """ doc """
        # models.Game.create("Test Game")
        models.Game.create(name="Test game")

    def setUp(self):
        """ doc """
        pass

    def test_income_works(self):
        """ doc """
        self.assertTrue(models.Game.objects.all()[0].name == "Test game" and len(models.Game.objects.all()) == 1)
