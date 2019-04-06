from .. import models
from .. import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .. import renderers
from profiles.models import Profile


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


class GameRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (renderers.GameJSONRenderer,)
    serializer_class = serializers.GameSerializer

    def retrieve(self, request, *args, **kwargs):
        game = models.Game.objects.get(join_token=self.kwargs['join_token'])
        serializer = self.serializer_class(game)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        """ Start game. """
        game = request.data.get('game', {})
        instance = models.Game.objects.get(join_token=self.kwargs['join_token'])
        serializer = self.serializer_class(instance, data=game)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
