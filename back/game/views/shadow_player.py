from .. import models
from .. import serializers
from rest_framework import generics


class ShadowPlayerList(generics.ListAPIView):
    """
    This view provides a `list` action with read_only enabled to the whole set of shadow_players.

    It is tied to the /api/shadow-players/ endpoint.
    """
    queryset = models.ShadowPlayer.objects.all()
    serializer_class = serializers.ShadowPlayerSerializer


class ShadowPlayerDetail(generics.RetrieveAPIView):
    """
    This view provides a `retrieve` action with read_only enabled to the shadow_player with given primary key.

    It is tied to the /api/shadow-player/<pk>/ endpoint.
    """
    queryset = models.ShadowPlayer.objects.all()
    serializer_class = serializers.ShadowPlayerSerializer
