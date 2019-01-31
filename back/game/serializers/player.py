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
    profile = serializers.SlugRelatedField(read_only=True, slug_field='user')
    balance = BalanceSerializer(read_only=True)
    production = ProductionSerializer(read_only=True)
    resources = ResourcesSerializer(read_only=True)

    class Meta:
        model = models.Player
        fields = ('id', 'game', 'profile', 'balance', 'production', 'resources')