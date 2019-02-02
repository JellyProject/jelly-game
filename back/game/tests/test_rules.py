from django.test import TestCase

from .. import models
from .. import game_settings as settings

class RulesTest(TestCase):
    """ Tests on the Building class """
    fixtures = ['profile', 'source_technologies', 'source_buildings']

    @classmethod
    def setUpTestData(cls):
        """ Set up a game with one player linked to a profile with username "John Doe". """
        profile = models.Profile.objects.get(user__username="John Doe")
        game = models.Game.create()
        game.add_player(profile)

    def setUp(self):
        pass

    def test_load_fixture(self):
        """ SourceBuilding load test. """
        building = models.SourceBuilding.objects.get(slug="usine-avancee")
        self.assertEqual(building.name, "Usine avancée")

    def test_building_purchase(self):
        """
            Building purchase test.

            The player purchases the first building defined in the sources.
        """
        player = models.Player.objects.get(profile__user__username="John Doe")
        first_building_init = player.buildings.get(slug='usine')
        source_building = first_building_init.source()
        self.assertLessEqual(source_building.cost, player.resources.money)
        (first_building_current, error_message) = player.purchase_building("usine")
        self.assertIs(error_message, "")
        self.assertIs(first_building_current.copies - first_building_init.copies, 1)
        self.assertIs(player.production.money,
                      settings.UM_INITIAL_PRODUCTION + source_building.money_modifier)
        self.assertIs(player.production.hydrocarbon,
                      settings.HYDROCARBON_INITIAL_PRODUCTION + source_building.hydrocarbon_modifier)
        self.assertIs(player.production.food,
                      settings.FOOD_INITIAL_PRODUCTION + source_building.food_modifier)
        self.assertIs(player.production.electricity,
                      settings.ELECTRICITY_INITIAL_PRODUCTION + source_building.electricity_modifier)
        self.assertIs(player.production.pollution,
                      settings.POLLUTION_INITIAL_PRODUCTION + source_building.pollution_modifier)
        self.assertIs(player.production.waste,
                      settings.WASTE_INITIAL_PRODUCTION + source_building.waste_modifier)
        self.assertIs(player.balance.economic,
                      settings.ECONOMIC_INITIAL_VALUE + source_building.economic_modifier)
        self.assertIs(player.balance.environmental,
                      settings.ENVIRONMENTAL_INITIAL_VALUE + source_building.environmental_modifier)
        self.assertIs(player.balance.social,
                      settings.SOCIAL_INITIAL_VALUE + source_building.social_modifier)

    def test_building_purchase_money_failure(self):
        """ Building purchase failure test : the player doesn't have enough money. """
        player = models.Player.objects.get(profile__user__username="John Doe")
        player.resources.money = 0
        balance_init = player.balance
        resources_init = player.resources
        production_init = player.production
        first_building_init = player.buildings.get(slug='usine')
        (first_building, error_message) = player.purchase_building("usine")
        self.assertEqual(error_message, "Fonds insuffisants")
        self.assertEqual(player.balance, balance_init)
        self.assertEqual(player.production, production_init)
        self.assertEqual(player.resources, resources_init)
        self.assertEqual(first_building, first_building_init)

    def test_building_purchase_tech_failure(self):
        """ Building purchase failure test : the player doesn't own a required technology. """
        player = models.Player.objects.get(profile__user__username="John Doe")
        balance_init = player.balance
        resources_init = player.resources
        production_init = player.production
        second_building_init = player.buildings.get(slug='usine-avancee')
        (second_building, error_message) = player.purchase_building("usine-avancee")
        self.assertEqual(error_message, "Technologie(s) nécessaire(s)")
        self.assertEqual(player.balance, balance_init)
        self.assertEqual(player.production, production_init)
        self.assertEqual(player.resources, resources_init)
        self.assertEqual(second_building, second_building_init)

    def test_building_purchase_era_failure(self):
        """ Building purchase failure test : the building belongs to a later era. """
        player = models.Player.objects.get(profile__user__username="John Doe")
        balance_init = player.balance
        resources_init = player.resources
        production_init = player.production
        third_building_init = player.buildings.get(slug='centrale-thermique')
        (third_building, error_message) = player.purchase_building("centrale-thermique")
        self.assertEqual(error_message, "Ère trop précoce")
        self.assertEqual(player.balance, balance_init)
        self.assertEqual(player.production, production_init)
        self.assertEqual(player.resources, resources_init)
        self.assertEqual(third_building, third_building_init)

    def test_building_unlock(self):
        """ Building unlock test. """
        player = models.Player.objects.get(profile__user__username="John Doe")
        player.resources.money = 1000
        advanced_factory = player.buildings.get(slug='usine-avancee')
        self.assertFalse(advanced_factory.unlocked)
        (technology, error) = player.purchase_technology("taylorisme")
        advanced_factory = player.buildings.get(slug='usine-avancee')
        self.assertTrue(advanced_factory.unlocked)