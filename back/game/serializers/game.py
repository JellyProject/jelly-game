from rest_framework import serializers
from .. import models


class GameSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    hydrocarbon_piles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    events = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Game
        fields = ('id', 'version', 'creation_date', 'last_save_date', 'turn', 'era', 'current_index_pile',
                  'players', 'hydrocarbon_piles', 'events')
