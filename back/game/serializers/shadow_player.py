from rest_framework import serializers
from .. import models

from .balance import BalanceSerializer
from .production import ProductionSerializer
from .resources import ResourcesSerializer


class ShadowPlayerSerializer(serializers.ModelSerializer):
    balance = BalanceSerializer(read_only=True)
    production = ProductionSerializer(read_only=True)
    resources = ResourcesSerializer(read_only=True)

    class Meta:
        model = models.ShadowPlayer
        fields = ('id',
                  'balance',
                  'production',
                  'resources')
