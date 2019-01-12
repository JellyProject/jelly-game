from rest_framework import generics

from .models import Resources
from .serializers import ResourcesSerializer


class ListResources(generics.ListCreateAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer


class DetailResources(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer
