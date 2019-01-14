from rest_framework import generics

from ..models import Building
from ..serializers import BuildingSerializer


class ListBuilding(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class DetailBuilding(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
