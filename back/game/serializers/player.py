from rest_framework import serializers
from .. import models
from .balance import BalanceSerializer
from .production import ProductionSerializer
from .resources import ResourcesSerializer


class PlayerSerializer(serializers.ModelSerializer):
    profile = serializers.ReadOnlyField(source='profile.user.username')
    balance = BalanceSerializer(read_only=True)
    production = ProductionSerializer(read_only=True)
    resources = ResourcesSerializer(read_only=True)

    class Meta:
        model = models.Player
        fields = ('id',
                  'game',
                  'profile',
                  'state')


class PlayerAddSerializer(serializers.ModelSerializer):
    join_token = serializers.UUIDField(write_only=True)
    state = PlayerStateSerializer(read_only=True)

    class Meta:
        model = models.Player
        fields = ('join_token', 'id', 'state') # TO_DO : add creation_date to player model
        read_only_fields = ['id']

    def validate(self, data):
        ''' Check if the current instance has valid data, and return it. '''
        join_token = data.get('join_token', None)

        if join_token is None:
            raise serializers.ValidationError(
                'A token is required.'
            )

        try:
            game = models.Game.objects.get(join_token=join_token)
        except:
            raise serializers.ValidationError(
                'The specified token is invalid.'
            )

        if game.is_live:
            raise serializers.ValidationError(
                'This game has already started.'
            )

        try:
            profile = Profile.objects.get(user=self.context['request'].user)
        except:
            raise serializers.ValidationError(
                'The logged in user is invalid.'
            )

        if game.players.filter(profile=profile): # This user has already joined the game
            raise serializers.ValidationError(
                'This player already exists.'
            )

        return {
            'join_token': game.join_token,
            'profile_pk': profile.pk
        }

    def create(self, validated_data):
        ''' Add a new player to the game with specified uuid. '''
        game = models.Game.objects.get(join_token=validated_data['join_token'])
        profile = Profile.objects.get(pk=validated_data['profile_pk'])
        return game.add_player(profile)
