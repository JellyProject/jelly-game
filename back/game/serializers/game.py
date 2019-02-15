from rest_framework import serializers
from .. import models
from .. import game_settings


class GameSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    hydrocarbon_piles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Game
        fields = ('id', 'version', 'creation_date', 'last_save_date', 'turn', 'era', 'current_index_pile',
                  'players', 'hydrocarbon_piles')

class GameCreateSerializer(serializers.ModelSerializer):
    """ Handle creation of a Game instance. """
    class Meta:
        model = models.Game
        fields = ('id', 'creation_date', 'is_live', 'version', 'join_token')
        read_only_fields = ('id', 'creation_date', 'is_live', 'join_token')

    def validate(self, data):
        ''' Check if the version is valid, and return the current instance. '''
        version = data.get('version', None)

        if version is None:
            raise serializers.ValidationError(
                'A version is required to create a game.'
            )

        if not version in game_settings.VERSIONS:
            raise serializers.ValidationError(
                'Invalid version.'
            )

        return {
            'version': version,
        }

    def create(self, validated_data):
        ''' Create a new Game '''
        return models.Game.create(**validated_data)


class GameJoinSerializer(serializers.Serializer):
    uuid = serializers.CharField(max_length=255)

    def validate(self, data):
        ''' Check if the current instance has valid data, and return it. '''
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                'A username is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # Check for a user that matches this username/password combination.
        user = authenticate(username=username, password=password)

        # Raise an exception if no user was found.
        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        # Return a dictionary of validated data, which is used by the `create`
        # and `update` methods for instance.
        return {
            'username': user.username,
            'email': user.email,
            'token': user.token
        }