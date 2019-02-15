from .. import models
from .. import serializers
from rest_framework import generics


class BuildingList(generics.ListAPIView):
    """
    This view provides a `list` action with read_only enabled to the set of buildings linked to the given player.

    It is tied to the /api/player/<player_pk>/building/ endpoint.
    """
    serializer_class = serializers.BuildingSerializer

    def get_queryset(self):
        return models.Building.objects.filter(player__pk=self.kwargs['player_pk'])


class BuildingDetail(generics.RetrieveAPIView):
    """
    This view provides a `retrieve` action with read_only enabled to the technology with given player and slug.

    It is tied to the /api/player/<player_pk>/building/<slug>/ endpoint.
    """
    serializer_class = serializers.BuildingSerializer
    lookup_field='slug'

    def get_queryset(self):
        return models.Building.objects.filter(player__pk=self.kwargs['player_pk'])