from rest_framework import serializers
from .. import models
from .. import game_settings


class GameSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    hydrocarbon_piles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Game
        fields = ('version', 'creation_date', 'last_save_date',
                  'turn', 'era', 'current_index_pile',
                  'players', 'hydrocarbon_piles',
                  'join_token', 'is_live')
        read_only_fields = ('version', 'creation_date', 'last_save_date',
                            'turn', 'era', 'current_index_pile',
                            'players', 'hydrocarbon_piles',
                            'join_token')

    def validate(self, data):
        """
        Check if is_live is valid, and return the current instance.

        validate() should only be used for updates.
        """
        is_live = data.get('is_live', None)

        if is_live is None:
            raise serializers.ValidationError(
                '"is_live" field missing.'
            )

        if not is_live:
            raise serializers.ValidationError(
                '"is_live" should be true.'
            )

        return {
            'is_live': is_live,
        }

    def update(self, instance, validated_data):
        """ Start a Game. """
        setattr(instance, "is_live", validated_data["is_live"])
        instance.save()
        return instance


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
