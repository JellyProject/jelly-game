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
     * Resource : set of technologies with given player.
     * Supported HTTP verbs : GET.
     * Related URI : api/player-states/<player_state_pk>/technologies
    """
    serializer_class = serializers.TechnologySerializer

    def get_queryset(self):
        try:
            return models.Technology.objects.filter(state__pk=self.kwargs['player_state_pk'])
        except models.Technology.DoesNotExist:
            raise TechnologyDoesNotExist


'''
class TechnologyDetail(generics.RetrieveUpdateAPIView):
    """
     * Resource : technology with given player and slug.
     * Supported HTTP verbs : GET, PUT, PATCH.
     * Related URI : api/player-states/<player_state_pk>/technologies/<slug>
    """
    serializer_class = serializers.TechnologySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return models.Technology.objects.filter(state__pk=self.kwargs['player_state_pk'])

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.data.get('purchased', False):
            return Response({"error":"'purchased' should be set to True"})
        (is_purchasable, error_message) = instance.is_purchasable()
        if not is_purchasable:
            return Response({"error":error_message})
        super(TechnologyDetail, self).update(request, *args, **kwargs)
        instance.trigger_post_purchase_effects()
'''


class TechnologyRetrieveUpdateAPIView(RetrieveUpdateAPIView):
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
        return Response(serializer.data, status=status.HTTP_200_OK)