from .. import models
from .. import serializers
from .. import renderers
from ..exceptions import SourceBuildingDoesNotExist
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class SourceBuildingList(generics.ListAPIView):
    """
     * Resource : a set of all source buildings with corresponding version.
     * Supported HTTP verbs : GET.
     * Related URI : /api/v1/source_building/<version>
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.SourceBuildingSerializer

    def list(self, request, *args, **kwargs):
        source_buildings = models.SourceBuilding.objects.filter(
            version=self.kwargs['version']
        )
        serializer = self.serializer_class(source_buildings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SourceBuildingDetail(generics.RetrieveAPIView):
    """
     * Resource : a source building with corresponding version and slug.
     * Supported HTTP verbs : GET.
     * Related URI : /api/v1/source_building/<version>/<slug:slug>
    """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (renderers.SourceBuildingJSONRenderer,)
    serializer_class = serializers.SourceBuildingSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            source_building = models.SourceBuilding.objects.get(
                version=self.kwargs['version'],
                slug=self.kwargs['slug']
            )
        except models.SourceBuilding.DoesNotExist:
            raise SourceBuildingDoesNotExist
        serializer = self.serializer_class(source_building)
        return Response(serializer.data, status=status.HTTP_200_OK)
