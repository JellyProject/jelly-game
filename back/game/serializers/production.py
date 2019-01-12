from rest_framework import serializers

from ..models import Production


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = Production
