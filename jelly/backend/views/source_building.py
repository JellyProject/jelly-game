from rest_framework import generics

from ..models import SourceBuilding
from ..serializers import SourceBuildingSerializer


class ListSourceBuilding(generics.ListCreateAPIView):
    queryset = SourceBuilding.objects.all()
    serializer_class = SourceBuildingSerializer


class DetailSourceBuilding(generics.RetrieveUpdateDestroyAPIView):
    queryset = SourceBuilding.objects.all()
    serializer_class = SourceBuildingSerializer
