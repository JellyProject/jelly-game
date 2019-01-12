from rest_framework import generics

from .models import SourceTechnology
from .serializers import SourceTechnologySerializer


class ListSourceTechnology(generics.ListCreateAPIView):
    queryset = SourceTechnology.objects.all()
    serializer_class = SourceTechnologySerializer


class DetailSourceTechnology(generics.RetrieveUpdateDestroyAPIView):
    queryset = SourceTechnology.objects.all()
    serializer_class = SourceTechnologySerializer
