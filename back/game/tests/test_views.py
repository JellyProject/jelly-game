from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .. import models
from .. import serializers


class SourceTechnologyTests(APITestCase):
    fixtures = ['source_technologies']

    def test_list_source_technologies(self):
        source_technologies = models.SourceTechnology.objects.all()
        serializer = serializers.SourceTechnologySerializer(source_technologies, many=True)
        response = self.client.get(reverse('source-technology-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_valid_list_version_source_technologies(self):
        source_technologies = models.SourceTechnology.objects.filter(version="jelly")
        serializer = serializers.SourceTechnologySerializer(source_technologies, many=True)
        response = self.client.get(reverse('source-technology-version-list', kwargs={"version": "jelly"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_invalid_list_version_source_technologies(self):
        response = self.client.get(reverse('source-technology-version-list', kwargs={"version": "raccoon"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_valid_detail_version_source_technology(self):
        source_technology = models.SourceTechnology.objects.get(version="jelly", slug="taylorisme")
        serializer = serializers.SourceTechnologySerializer(source_technology)
        response = self.client.get(reverse('source-technology-version-detail',
                                           kwargs={"version": "jelly", "slug": "taylorisme"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_invalid_detail__version_source_technology(self):
        response = self.client.get(reverse('source-technology-version-detail',
                                           kwargs={"version": "jelly", "slug": "head-patting"}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class SourceBuildingTests(APITestCase):
    fixtures = ['source_technologies', 'source_buildings']

    def test_list_source_buildings(self):
        source_buildings = models.SourceBuilding.objects.all()
        serializer = serializers.SourceBuildingSerializer(source_buildings, many=True)
        response = self.client.get(reverse('source-building-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_valid_list_version_source_buildings(self):
        source_buildings = models.SourceBuilding.objects.filter(version="jelly")
        serializer = serializers.SourceBuildingSerializer(source_buildings, many=True)
        response = self.client.get(reverse('source-building-version-list', kwargs={"version": "jelly"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_invalid_list_version_source_buildings(self):
        response = self.client.get(reverse('source-building-version-list', kwargs={"version": "raccoon"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_valid_detail_version_source_building(self):
        source_building = models.SourceBuilding.objects.get(version="jelly", slug="usine")
        serializer = serializers.SourceBuildingSerializer(source_building)
        response = self.client.get(reverse('source-building-version-detail',
                                           kwargs={"version": "jelly", "slug": "usine"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_invalid_detail_version_source_building(self):
        response = self.client.get(reverse('source-building-version-detail',
                                           kwargs={"version": "jelly", "slug": "head-patting"}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ProfileTests(APITestCase):
    """ TO DO : USER/PROFILE CLEAN IMPLEMENTATION """
    fixtures = ['users', 'games', 'players']

    def test_list_profiles(self):
        profiles = models.Profile.objects.all()
        serializer = serializers.ProfileSerializer(profiles, many=True)
        response = self.client.get(reverse('profile-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_valid_detail_profile(self):
        profile = models.Profile.objects.get(user__username="John Doe")
        serializer = serializers.ProfileSerializer(profile)
        response = self.client.get(reverse('profile-detail', kwargs={"username": "John Doe"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    """def test_invalid_detail_profile(self):
        response = self.client.get(reverse('profile-detail', kwargs={"username": "Jane Doe"}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)"""


class GameTests(APITestCase):
    fixtures = ['users', 'games', 'players']

    def test_list_games(self):
        games = models.Game.objects.all()
        serializer = serializers.GameSerializer(games, many=True)
        response = self.client.get(reverse('game-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_valid_detail_game(self):
        game = models.Game.objects.get(pk=1)
        serializer = serializers.GameSerializer(game)
        response = self.client.get(reverse('game-detail', kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_invalid_detail_game(self):
        response = self.client.get(reverse('game-detail', kwargs={"pk": 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class PlayerTests(APITestCase):
    fixtures = ['users', 'games', 'players']

    def test_list_players(self):
        players = models.Player.objects.all()
        serializer = serializers.PlayerSerializer(players, many=True)
        response = self.client.get(reverse('player-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_valid_detail_player(self):
        player = models.Player.objects.get(pk=1)
        serializer = serializers.PlayerSerializer(player)
        response = self.client.get(reverse('player-detail', kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_invalid_detail_player(self):
        response = self.client.get(reverse('player-detail', kwargs={"pk": 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TechnologyTests(APITestCase):
    fixtures = ['source_technologies', 'source_buildings', 'users', 'games', 'players']

    def test_list_technologies(self):
        technologies = models.Technology.objects.all()
        serializer = serializers.TechnologySerializer(technologies, many=True)
        response = self.client.get(reverse('technology-list', kwargs={"state_pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_valid_detail_technology(self):
        technology = models.Technology.objects.get(slug="taylorisme")
        serializer = serializers.TechnologySerializer(technology)
        response = self.client.get(reverse('technology-detail', kwargs={"state_pk": 1, "slug": "taylorisme"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_invalid_detail_technology(self):
        response = self.client.get(reverse('technology-detail', kwargs={"state_pk": 1, "slug": "head-patting"}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """def test_valid_update_technology(self):
        technology = models.Technology.objects.get(slug="taylorisme")
        technology.player.resources.money = 50
        technology.player.resources.save()
        response = self.client.patch(reverse('technology-detail', kwargs={"player_pk": 1, "slug": "taylorisme"}),
                                     {'purchased': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(models.Technology.objects.get(slug="taylorisme").purchased)
        self.assertEqual(technology.player.resources.money,
                         50 - models.SourceTechnology.objects.get(slug="taylorisme").cost)"""


class BuildingTests(APITestCase):
    fixtures = ['users', 'games', 'players']

    def test_list_buildings(self):
        buildings = models.Building.objects.all()
        serializer = serializers.BuildingSerializer(buildings, many=True)
        response = self.client.get(reverse('building-list', kwargs={"state_pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_valid_detail_building(self):
        building = models.Building.objects.get(pk=1)
        serializer = serializers.BuildingSerializer(building)
        response = self.client.get(reverse('building-detail', kwargs={"state_pk": 1, "slug": "usine"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_invalid_detail_building(self):
        response = self.client.get(reverse('building-detail', kwargs={"state_pk": 1, "slug": "head-patting"}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
