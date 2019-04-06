from .. import models
from .. import serializers
from .. import renderers
from ..exceptions import TechnologyDoesNotExist
from rest_framework import generics
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class TechnologyList(generics.ListAPIView):
    """
     * Resource : a set of all technologies with corresponding player.
     * Supported HTTP verbs : GET.
     * Related URI : api/v1/player-states/<int:player_state_pk>/technologies
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.TechnologySerializer

    def list(self, request, *args, **kwargs):
        technologies = models.Technology.objects.filter(
            state__pk=self.kwargs['player_state_pk']
        )
        serializer = self.serializer_class(technologies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TechnologyRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """
     * Resource : a technology with corresponding player and source slug.
     * Supported HTTP verbs : GET, PUT, PATCH.
     * Related URI : api/v1/player-states/<int:player_state_pk>/technologies/<slug:source_slug>
    """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (renderers.TechnologyJSONRenderer,)
    serializer_class = serializers.TechnologySerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            technology = models.Technology.objects.get(
                state__pk=self.kwargs['player_state_pk'],
                source__slug=self.kwargs['source_slug']
            )
        except models.Technology.DoesNotExist:
            raise TechnologyDoesNotExist
        serializer = self.serializer_class(technology)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        """ Purchase technology. """
        technology = request.data.get('technology', {})
        try:
            instance = models.Technology.objects.get(
                state__pk=self.kwargs['player_state_pk'],
                source__slug=self.kwargs['source_slug']
            )
        except models.Technology.DoesNotExist:
            raise TechnologyDoesNotExist
        serializer = self.serializer_class(instance, data=technology)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        instance.trigger_post_purchase_effects()
        return Response(serializer.data, status=status.HTTP_200_OK)