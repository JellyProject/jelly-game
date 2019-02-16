from .. import models
from .. import serializers
from rest_framework import generics


class SourceTechnologyList(generics.ListAPIView):
    """
    This view provides a `list` action with read_only enabled to the whole set of source technologies.

    It is tied to the /api/source_technology/ endpoint.
    """
    queryset = models.SourceTechnology.objects.all()
    serializer_class = serializers.SourceTechnologySerializer


class SourceTechnologyVersionList(generics.ListAPIView):
    """
    This view provides a `list` action with read_only enabled to the set of source technologies with given version.

    It is tied to the /api/source_technology/<version>/ endpoint.
    """
    serializer_class = serializers.SourceTechnologySerializer

    def get_queryset(self):
        return models.SourceTechnology.objects.filter(version=self.kwargs['version'])


class SourceTechnologyVersionDetail(generics.RetrieveAPIView):
    """
    This view provides a `retrieve` action with read_only enabled to the source technology with given version and slug.

    It is tied to the /api/source_technology/<version>/<slug>/ endpoint.
    """
    serializer_class = serializers.SourceTechnologySerializer
    lookup_field='slug'

    def get_queryset(self):
        return models.SourceTechnology.objects.filter(version=self.kwargs['version'])