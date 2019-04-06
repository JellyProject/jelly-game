from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer
from .exceptions import ProfileDoesNotExist


class ProfileList(ListAPIView):
    """
     * Resource : a set of all profiles.
     * Supported HTTP verbs : GET.
     * Related URI : api/v1/profiles/
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def list(self, request, *args, **kwargs):
        profiles = Profile.objects.all()
        serializer = self.serializer_class(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileRetrieveAPIView(RetrieveAPIView):
    """
        This view provides a `retrieve` action with read_only enabled to the game with given primary key.

        It is tied to the /api/v1/profiles/<username> endpoint.
    """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.select_related('user').get(
                user__username=self.kwargs.get("username")
            )
        except Profile.DoesNotExist:
            raise ProfileDoesNotExist
        serializer = self.serializer_class(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
