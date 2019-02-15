from django.test import TestCase

from .. import models
from .. import game_settings as settings
from profiles.models import Profile



class RulesTest(TestCase):
    """ Tests on the Building class """
    fixtures = ['users', 'source_technologies', 'source_buildings', 'source_events']

    @classmethod
    def setUpTestData(cls):
        """ Set up a game with one player linked to a profile with username "John Doe". """
        profile = Profile.objects.get(user__username="JohnDoe")
        game = models.Game.create()
        game.add_player(profile)

    def setUp(self):
        self.player = models.Player.objects.get(profile__user__username="JohnDoe")

    def test_load_fixture(self):
        """ SourceBuilding load test. """
        building = models.SourceBuilding.objects.get(slug="usine-avancee")
        self.assertEqual(building.name, "Usine avancée")

    def test_building_purchase(self):
        """ Building purchase test : the player purchases a factory. """
        first_building_init = self.player.state.buildings.get(slug='usine')
        source_building = first_building_init.source()
        self.assertLessEqual(source_building.cost, self.player.state.resources.money)
        (first_building_current, error_message) = self.player.purchase_building("usine")
        self.assertIs(error_message, "")
        self.assertIs(first_building_current.copies - first_building_init.copies, 1)
        self.assertIs(self.player.state.production.money,
                      settings.UM_INITIAL_PRODUCTION + source_building.money_modifier)
        self.assertIs(self.player.state.production.hydrocarbon,
                      settings.HYDROCARBON_INITIAL_PRODUCTION + source_building.hydrocarbon_modifier)
        self.assertIs(self.player.state.production.food,
                      settings.FOOD_INITIAL_PRODUCTION + source_building.food_modifier)
        self.assertIs(self.player.state.production.electricity,
                      settings.ELECTRICITY_INITIAL_PRODUCTION + source_building.electricity_modifier)
        self.assertIs(self.player.state.production.pollution,
                      settings.POLLUTION_INITIAL_PRODUCTION + source_building.pollution_modifier)
        self.assertIs(self.player.state.production.waste,
                      settings.WASTE_INITIAL_PRODUCTION + source_building.waste_modifier)
        self.assertIs(self.player.state.balance.economic,
                      settings.ECONOMIC_INITIAL_VALUE + source_building.economic_modifier)
        self.assertIs(self.player.state.balance.environmental,
                      settings.ENVIRONMENTAL_INITIAL_VALUE + source_building.environmental_modifier)
        self.assertIs(self.player.state.balance.social,
                      settings.SOCIAL_INITIAL_VALUE + source_building.social_modifier)

    def test_building_purchase_money_failure(self):
        """ Building purchase failure test : the player doesn't have enough money. """
        self.player.state.resources.money = 0
        balance_init = self.player.state.balance
        resources_init = self.player.state.resources
        production_init = self.player.state.production
        first_building_init = self.player.state.buildings.get(slug='usine')
        a = self.player.state.purchase_building("usine")
        (first_building, error_message) = a
        self.assertEqual(error_message, "Fonds insuffisants")
        self.assertEqual(self.player.state.balance, balance_init)
        self.assertEqual(self.player.state.production, production_init)
        self.assertEqual(self.player.state.resources, resources_init)
        self.assertEqual(first_building, first_building_init)

    def test_building_purchase_tech_failure(self):
        """ Building purchase failure test : the player doesn't own a required technology. """
        balance_init = self.player.balance
        resources_init = self.player.resources
        production_init = self.player.production
        second_building_init = self.player.buildings.get(slug='usine-avancee')
        (second_building, error_message) = self.player.purchase_building("usine-avancee")
        self.assertEqual(error_message, "Technologie(s) nécessaire(s)")
        self.assertEqual(self.player.balance, balance_init)
        self.assertEqual(self.player.production, production_init)
        self.assertEqual(self.player.resources, resources_init)
        self.assertEqual(second_building, second_building_init)

    def test_building_purchase_era_failure(self):
        """ Building purchase failure test : the building belongs to a later era. """
        balance_init = self.player.state.balance
        resources_init = self.player.state.resources
        production_init = self.player.state.production
        third_building_init = self.player.state.buildings.get(slug='centrale-thermique')
        (third_building, error_message) = self.player.purchase_building("centrale-thermique")
        self.assertEqual(error_message, "Ère trop précoce")
        self.assertEqual(self.player.state.balance, balance_init)
        self.assertEqual(self.player.state.production, production_init)
        self.assertEqual(self.player.state.resources, resources_init)
        self.assertEqual(third_building, third_building_init)

    def test_building_unlock(self):
        """ Building unlock test. """
        self.player.resources.money = 1000
        advanced_factory = self.player.state.buildings.get(slug='usine-avancee')
        self.assertFalse(advanced_factory.unlocked)
        (technology, error) = self.player.purchase_technology("taylorisme")
        self.assertTrue(advanced_factory.unlocked)

    """ Tests on the Shadowplayer class """

    def test_shadowplayer_recover(self):
        """ ShadowPlayer Recover test. """
        self.shadowplayer = models.ShadowPlayer.objects.get(player=self.player)
        building_init = self.player.state.buildings.get(slug='centrale-thermique')
        self.shadowplayer.recover(self.player)
        self.assertIs(building_init.copies, 0)
