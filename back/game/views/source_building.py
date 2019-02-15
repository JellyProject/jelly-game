from .. import models
from .. import serializers
from rest_framework import generics


class SourceBuildingList(generics.ListAPIView):
    """
    This view provides a `list` action with read_only enabled to the whole set of source buildings.

    It is tied to the /api/source_building/ endpoint.
    """
    queryset = models.SourceBuilding.objects.all()
    serializer_class = serializers.SourceBuildingSerializer


class SourceBuildingVersionList(generics.ListAPIView):
    """
    This view provides a `list` action with read_only enabled to the set of source buildings with given version.

    It is tied to the /api/source_building/<version>/ endpoint.
    """
    serializer_class = serializers.SourceBuildingSerializer

    def get_queryset(self):
        return models.SourceBuilding.objects.filter(version=self.kwargs['version'])


class SourceBuildingVersionDetail(generics.RetrieveAPIView):
    """
    This view provides a `retrieve` action with read_only enabled to the source building with given version and slug.

    It is tied to the /api/source_building/<version>/<slug>/ endpoint.
    """
    serializer_class = serializers.SourceBuildingSerializer
    lookup_field='slug'

    def get_queryset(self):
        return models.SourceBuilding.objects.filter(version=self.kwargs['version'])