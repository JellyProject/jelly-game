from .. import models
from .. import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

class ProfileList(generics.ListAPIView):
    """
    This view provides a `list` action with read_only enabled to the whole set of profiles.

    It is tied to the /api/profile/ endpoint.
    """
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


class ProfileDetail(generics.RetrieveAPIView):
    """
    This view provides a `retrieve` action with read_only enabled to the game with given primary key.

    It is tied to the /api/profile/<username>/ endpoint.
    """
    serializer_class = serializers.ProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        username = self.kwargs.get("username")
        try:
            instance = models.Profile.objects.get(user__username=username)
        except:
            raise NotFound
        print("Hello")
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
