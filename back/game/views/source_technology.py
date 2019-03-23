from .. import models
from .. import serializers
from .. import renderers
from ..exceptions import SourceTechnologyDoesNotExist
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class SourceTechnologyList(generics.ListAPIView):
    """
     * Resource : a set of all source technologies with corresponding version.
     * Supported HTTP verbs : GET.
     * Related URI : /api/v1/source_technology/<version>
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.SourceTechnologySerializer

    def list(self, request, *args, **kwargs):
        source_technologies = models.SourceTechnology.objects.filter(
            version=self.kwargs['version']
        )
        serializer = self.serializer_class(source_technologies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SourceTechnologyDetail(generics.RetrieveAPIView):
    """
     * Resource : a source technology with corresponding version and slug.
     * Supported HTTP verbs : GET.
     * Related URI : /api/v1/source_technology/<version>/<slug:slug>
    """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (renderers.SourceTechnologyJSONRenderer,)
    serializer_class = serializers.SourceTechnologySerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            source_technology = models.SourceTechnology.objects.get(
                version=self.kwargs['version'],
                slug=self.kwargs['slug']
            )
        except models.SourceTechnology.DoesNotExist:
            raise SourceTechnologyDoesNotExist
        serializer = self.serializer_class(source_technology)
        return Response(serializer.data, status=status.HTTP_200_OK)
