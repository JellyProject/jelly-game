from .. import models
from .. import serializers
from rest_framework import generics


class PlayerStateList(generics.ListAPIView):
    """
    This view provides a `list` action with read_only enabled to the whole set of players.

    It is tied to the /api/player-states/ endpoint.
    """
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerStateSerializer


class PlayerStateDetail(generics.RetrieveAPIView):
    """
    This view provides a `retrieve` action with read_only enabled to the player with given primary key.

    It is tied to the /api/player-states/<pk>/ endpoint.
    """
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerStateSerializer
