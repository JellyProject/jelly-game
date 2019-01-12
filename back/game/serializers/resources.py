from rest_framework import serializers

from ..models import Resources


class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = Resources
