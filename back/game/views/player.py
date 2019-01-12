from rest_framework import generics

from ..models import Player
from ..serializers import PlayerSerializer


class ListPlayer(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class DetailPlayer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
