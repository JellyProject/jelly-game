from rest_framework import serializers
from .. import models


class SourceBuildingSerializer(serializers.ModelSerializer):
    parent_technology = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = models.SourceBuilding
        fields = '__all__'
