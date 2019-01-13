from rest_framework import serializers

from ..models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Player
