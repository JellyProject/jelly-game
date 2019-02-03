from .. import models
from .. import serializers
from rest_framework import generics

class GameList(generics.ListAPIView):
    """
    This view provides a `list` action with read_only enabled to the whole set of games.

    It is tied to the /api/game/ endpoint.
    """
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer


class GameDetail(generics.RetrieveAPIView):
    """
    This view provides a `retrieve` action with read_only enabled to the game with given primary key.

    It is tied to the /api/game/<pk>/ endpoint.
    """
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer