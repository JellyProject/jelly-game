from rest_framework import generics

from .models import Game
from .serializers import GameSerializer


class ListGame(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class DetailGame(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
