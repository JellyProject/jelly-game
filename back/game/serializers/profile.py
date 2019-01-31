from rest_framework import serializers
from .. import models


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    players = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Profile
        fields = ('username', 'players')