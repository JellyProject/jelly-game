from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer
from .exceptions import ProfileDoesNotExist


class ProfileRetrieveAPIView(RetrieveAPIView):
    """
        This view provides a `retrieve` action with read_only enabled to the game with given primary key.

        It is tied to the /api/v1/profiles/<username> endpoint.
    """
    permission_classes = (AllowAny,)
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