from .. import models
from .. import serializers
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .. import renderers
from profiles.models import Profile


class GameList(generics.ListAPIView):
    """
    This view provides a `list` action with read_only enabled to the whole set of games.

    It is tied to the /api/game/ endpoint.
    """
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer


class GameDetail(generics.RetrieveAPIView):
    """
    This view provides a `retrieve` action with read_only enabled to the game with given primary key.

    It is tied to the /api/game/<pk>/ endpoint.
    """
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer


class GameCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (renderers.GameJSONRenderer,)
    serializer_class = serializers.GameCreateSerializer

    def post(self, request):
        game = request.data.get('game', {})
        serializer = self.serializer_class(data=game)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        game = models.Game.objects.get(pk=serializer.data['id'])
        profile = Profile.objects.get(user=request.user)
        game.add_player(profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GameJoinAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (renderers.GameJSONRenderer,)
    serializer_class = serializers.GameJoinSerializer

    def post(self, request):
        game = request.data.get('game', {})
        serializer = self.serializer_class(data=game)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)