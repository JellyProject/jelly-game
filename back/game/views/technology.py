from rest_framework import generics

from ..models import Technology
from ..serializers import TechnologySerializer


class ListTechnology(generics.ListCreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


class DetailTechnology(generics.RetrieveUpdateDestroyAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
