from rest_framework import serializers

from ..models import SourceTechnology


class SourceTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = SourceTechnology
