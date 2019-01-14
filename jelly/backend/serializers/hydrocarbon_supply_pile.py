from rest_framework import serializers

from ..models import HydrocarbonSupplyPile


class HydrocarbonSupplyPileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = HydrocarbonSupplyPile