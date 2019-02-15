from rest_framework import serializers
from .. import models
from .balance import BalanceSerializer
from .production import ProductionSerializer
from .resources import ResourcesSerializer


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