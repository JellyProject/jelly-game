from .. import models
from .. import serializers
from .. import renderers
from ..exceptions import BuildingDoesNotExist
from rest_framework import generics
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class BuildingList(generics.ListAPIView):
    """
     * Resource : a set of all buildings with corresponding player.
     * Supported HTTP verbs : GET.
     * Related URI : api/v1/player-states/<int:player_state_pk>/buildings
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.BuildingSerializer

    def list(self, request, *args, **kwargs):
        buildings = models.Building.objects.filter(
            state__pk=self.kwargs['player_state_pk']
        )
        serializer = self.serializer_class(buildings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BuildingRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """
     * Resource : a building with corresponding player and source slug.
     * Supported HTTP verbs : GET, PUT, PATCH.
     * Related URI : api/v1/player-states/<int:player_state_pk>/buildings/<slug:source_slug>
    """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (renderers.BuildingJSONRenderer,)
    serializer_class = serializers.BuildingSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            building = models.Building.objects.get(
                state__pk=self.kwargs['player_state_pk'],
                source__slug=self.kwargs['source_slug']
            )
        except models.Building.DoesNotExist:
            raise BuildingDoesNotExist
        serializer = self.serializer_class(building)
        return Response(serializer.data, status=status.HTTP_200_OK)