from rest_framework import serializers

from ..models import SourceBuilding


class SourceBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SourceBuilding
