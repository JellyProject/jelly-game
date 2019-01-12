from rest_framework import serializers

from ..models import SourceEvent


class SourceEventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = SourceEvent
