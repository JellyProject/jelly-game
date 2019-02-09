from rest_framework import serializers
from .. import models

from .player_state import PlayerStateSerializer
from .player import PlayerSerializer


class ShadowPlayerSerializer(serializers.ModelSerializer):
    state = PlayerStateSerializer(read_only=True)
    player = PlayerSerializer(read_only=True)

    class Meta:
        model = models.Player
        fields = ('id',
                  'state',
                  'player')
