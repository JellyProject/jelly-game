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


class PlayerList(generics.ListAPIView):
    """
    This view provides a `list` action with read_only enabled to the whole set of players.

    It is tied to the /api/player/ endpoint.
    """
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer


class PlayerDetail(generics.RetrieveAPIView):
    """
    This view provides a `retrieve` action with read_only enabled to the player with given primary key.

    It is tied to the /api/player/<pk>/ endpoint.
    """
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer


class PlayerAddAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (renderers.PlayerJSONRenderer,)
    serializer_class = serializers.PlayerAddSerializer

    def post(self, request):
        player = request.data.get('player', {})
        serializer = self.serializer_class(data=player, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)