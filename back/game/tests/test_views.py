from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate
from .. import models
from .. import serializers
from authentication.models import User


class SourceTechnologyTests(APITestCase):
    fixtures = ['source_technologies', 'users']

    def setUp(self):
        user = User.objects.all()[0] # Requests will be authenticated by this user.
        self.client.force_authenticate(user=user)

    def test_valid_list_source_technologies(self):
        source_technologies = models.SourceTechnology.objects.filter(version="jelly")
        serializer = serializers.SourceTechnologySerializer(source_technologies, many=True)
        response = self.client.get(reverse('source-technology-list', kwargs={"version": "jelly"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_invalid_list_source_technologies(self):
        response = self.client.get(reverse('source-technology-list', kwargs={"version": "raccoon"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_valid_detail_source_technology(self):
        source_technology = models.SourceTechnology.objects.get(version="jelly", slug="taylorisme")
        serializer = serializers.SourceTechnologySerializer(source_technology)
        response = self.client.get(reverse(
            'source-technology-detail',
            kwargs={"version": "jelly", "slug": "taylorisme"}
        ))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_invalid_detail_source_technology(self):
        response = self.client.get(reverse(
            'source-technology-detail',
            kwargs={"version": "jelly", "slug": "head-patting"}
        ))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class SourceBuildingTests(APITestCase):
    fixtures = ['source_technologies', 'source_buildings', 'users']

    def setUp(self):
        user = User.objects.all()[0] # Requests will be authenticated by this user.
        self.client.force_authenticate(user=user)

    def test_valid_list_source_buildings(self):
        source_buildings = models.SourceBuilding.objects.filter(version="jelly")
        serializer = serializers.SourceBuildingSerializer(source_buildings, many=True)
        response = self.client.get(reverse('source-building-list', kwargs={"version": "jelly"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_invalid_list_source_buildings(self):
        response = self.client.get(reverse('source-building-list', kwargs={"version": "raccoon"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_valid_detail_source_building(self):
        source_building = models.SourceBuilding.objects.get(version="jelly", slug="usine")
        serializer = serializers.SourceBuildingSerializer(source_building)
        response = self.client.get(reverse(
            'source-building-detail',
            kwargs={"version": "jelly", "slug": "usine"}
        ))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_invalid_detail_source_building(self):
        response = self.client.get(reverse(
            'source-building-detail',
            kwargs={"version": "jelly", "slug": "head-patting"}
        ))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


'''
class ProfileTests(APITestCase):
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
'''


'''
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
'''

'''
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
'''


class TechnologyTests(APITestCase):
    fixtures = ['source_technologies', 'source_buildings', 'users', 'games', 'players']

    def setUp(self):
        user = User.objects.all()[0] # Requests will be authenticated by this user.
        self.client.force_authenticate(user=user)

    def test_list_technologies(self):
        technologies = models.Technology.objects.all()
        serializer = serializers.TechnologySerializer(technologies, many=True)
        response = self.client.get(reverse('technology-list', kwargs={"player_state_pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_valid_detail_technology(self):
        technology = models.Technology.objects.get(source__slug="taylorisme")
        serializer = serializers.TechnologySerializer(technology)
        response = self.client.get(reverse(
            'technology-detail',
            kwargs={"player_state_pk": 1, "source_slug": "taylorisme"}
        ))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_invalid_detail_technology(self):
        response = self.client.get(reverse(
            'technology-detail',
            kwargs={"player_state_pk": 1, "source_slug": "head-patting"}
        ))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_technology(self):
        technology = models.Technology.objects.get(source__slug="taylorisme", state__pk=1)
        technology.state.resources.money = technology.source.cost
        technology.state.resources.save()
        response = self.client.put(reverse(
            'technology-detail',
            kwargs={"player_state_pk": 1, "source_slug": "taylorisme"}
        ), {'technology': {'purchased': True}})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(models.Technology.objects.get(source__slug="taylorisme", state__pk=1).purchased)
        self.assertEqual(models.Resources.objects.get(state__pk=1).money, 0)

"""
class BuildingTests(APITestCase):
    fixtures = ['source_technologies', 'source_buildings', 'users', 'games', 'players']

    def setUp(self):
        user = User.objects.all()[0] # Requests will be authenticated by this user.
        self.client.force_authenticate(user=user)

    def test_list_buildings(self):
        buildings = models.Building.objects.all()
        serializer = serializers.BuildingSerializer(buildings, many=True)
        response = self.client.get(reverse('building-list', kwargs={"player_state_pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_valid_detail_building(self):
        building = models.Building.objects.get(source__slug="usine")
        serializer = serializers.BuildingSerializer(building)
        response = self.client.get(reverse(
            'building-detail',
            kwargs={"player_state_pk": 1, "source_slug": "usine"}
        ))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_invalid_detail_building(self):
        response = self.client.get(reverse(
            'building-detail',
            kwargs={"player_state_pk": 1, "source_slug": "bird-nest"}
        ))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
"""