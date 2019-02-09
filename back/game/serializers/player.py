from rest_framework import serializers
from .. import models

from .player_state import PlayerStateSerializer


class PlayerSerializer(serializers.ModelSerializer):
    profile = serializers.ReadOnlyField(source='profile.user.username')
    state = PlayerStateSerializer(read_only=True)

    class Meta:
        model = models.Player
        fields = ('id',
                  'game',
                  'profile',
                  'state')
