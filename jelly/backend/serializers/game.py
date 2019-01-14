from rest_framework import serializers

from ..models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Game
