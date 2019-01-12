from rest_framework import serializers

from ..models import Building


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = Building
