from django.test import TestCase

from .. import models
from .. import game_settings as constant

class BuildingTest(TestCase):
    """ Tests on the Building class """
    fixtures = ['sample_data', 'buildings', 'technologies']

    def setUp(self):
        pass

    def test_load_fixture(self):
        """ SourceBuilding load test """
        building = models.SourceBuilding.objects.get(slug="usine-avancee")
        self.assertEqual(building.name, "Usine avancée")

    def test_building_purchase(self):
        """ Building purchase test """
        player = models.Player.objects.get(profile__user__username="Username")
        player.purchase_building(1)