from rest_framework import generics

from .models import HydrocarbonSupplyPile
from .serializers import HydrocarbonSupplyPileSerializer


class ListHydrocarbonSupplyPile(generics.ListCreateAPIView):
    queryset = HydrocarbonSupplyPile.objects.all()
    serializer_class = HydrocarbonSupplyPileSerializer


class DetailHydrocarbonSupplyPile(generics.RetrieveUpdateDestroyAPIView):
    queryset = HydrocarbonSupplyPile.objects.all()
    serializer_class = HydrocarbonSupplyPileSerializer
