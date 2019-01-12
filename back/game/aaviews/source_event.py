from rest_framework import generics

from .models import SourceEvent
from .serializers import SourceEventSerializer


class ListSourceEvent(generics.ListCreateAPIView):
    queryset = SourceEvent.objects.all()
    serializer_class = SourceEventSerializer


class DetailSourceEvent(generics.RetrieveUpdateDestroyAPIView):
    queryset = SourceEvent.objects.all()
    serializer_class = SourceEventSerializer
