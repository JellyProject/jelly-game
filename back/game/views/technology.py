from .. import models
from .. import serializers
from rest_framework import generics


class TechnologyList(generics.ListAPIView):
    """
    This view provides a `list` action with read_only enabled to the set of technologies linked to the given player.

    It is tied to the /api/player/<player_pk>/technology/ endpoint.
    """
    serializer_class = serializers.TechnologySerializer

    def get_queryset(self):
        return models.Technology.objects.filter(player__pk=self.kwargs['player_pk'])


class TechnologyDetail(generics.RetrieveAPIView):
    """
    This view provides a `retrieve` action with read_only enabled to the technology with given player and slug.

    It is tied to the /api/player/<player_pk>/technology/<slug>/ endpoint.
    """
    serializer_class = serializers.TechnologySerializer
    lookup_field='slug'

    def get_queryset(self):
        return models.Technology.objects.filter(player__pk=self.kwargs['player_pk'])