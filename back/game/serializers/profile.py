from rest_framework import serializers

from ..models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = Profile
