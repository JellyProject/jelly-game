# from django.http import HttpResponse, Http404
# from django.shortcuts import render, redirect
# from datetime import datetime

from rest_framework import generics

from .models import Game
from .serializers import GameSerializer

from .models import Player
from .serializers import PlayerSerializer


class ListGame(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class DetailGame(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class ListPlayer(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class DetailPlayer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
