from rest_framework import serializers

from ..models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'version',
            'era',
            'current_index_pile',
            'source_buildings',

            'players',
            'hydrocarbon_piles',
        )
        model = Game
