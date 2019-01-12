from rest_framework import serializers

from .models import Balance
from .models import Building
from .models import Event
from .models import Game
from .models import HydrocarbonSupplyPile
from .models import Player
from .models import Production
from .models import Profile
from .models import Resources
from .models import SourceBuilding
from .models import SourceEvent
from .models import SourceTechnology
from .models import Technology


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = Balance


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = Building


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = Event


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'version',
            'era',
            'current_index_pile',
            'source_buildings',
        )
        model = Game


class HydrocarbonSupplyPileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = HydrocarbonSupplyPile


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'game',
            'profile',
        )
        model = Player


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = Production


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = Profile


class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = Resources


class SourceBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = SourceBuilding


class SourceEventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = SourceEvent


class SourceTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = SourceTechnology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = Technology
