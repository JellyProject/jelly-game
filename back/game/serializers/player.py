from rest_framework import serializers
from .. import models

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resources
        fields = ('money',
                  'hydrocarbon')


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Production
        fields = ('money',
                  'hydrocarbon',
                  'food',
                  'electricity',
                  'pollution',
                  'waste')


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Balance
        fields = ('economic',
                  'social',
                  'environmental')


class PlayerSerializer(serializers.ModelSerializer):
    profile = serializers.ReadOnlyField(source='profile.user.username')
    balance = BalanceSerializer(read_only=True)
    production = ProductionSerializer(read_only=True)
    resources = ResourcesSerializer(read_only=True)

    class Meta:
        model = models.Player
        fields = ('id',
                  'game',
                  'profile',
                  'balance',
                  'production',
                  'resources')