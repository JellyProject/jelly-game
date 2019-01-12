from rest_framework import generics

from .models import Production
from .serializers import ProductionSerializer


class ListProduction(generics.ListCreateAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer


class DetailProduction(generics.RetrieveUpdateDestroyAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer
