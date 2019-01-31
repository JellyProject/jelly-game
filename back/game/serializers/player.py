from rest_framework import serializers
from .. import models

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resources
        fields = '__all__'


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resources
        fields = '__all__'


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resources
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    profile = serializers.SlugRelatedField(read_only=True, slug_field='user.username')
    resources = ResourcesSerializer(read_only=True)
    hydrocarbon_piles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    events = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Game
        fields = ('id', 'version', 'creation_date', 'last_save_date', 'turn', 'era', 'current_index_pile',
                  'players', 'hydrocarbon_piles', 'events')