from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User
from profiles.serializers import ProfileSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'token']

    def create(self, validated_data):
        ''' Create a new User '''
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

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


class UserSerializer(serializers.ModelSerializer):
    """ Handle serialization and deserialization of User objects. """

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    profile = ProfileSerializer(write_only=True)
    motto = serializers.CharField(source='profile.motto', read_only=True)
    image = serializers.CharField(source='profile.image', read_only=True)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password', 'token', 'profile', 'motto', 'image'
        )
        read_only_fields = ('token',)

    def update(self, instance, validated_data):
        """ Perform an update on a User. """
        # Remove password from data, since it should only be handled with
        # set_password().
        password = validated_data.pop('password', None)
        profile_data = validated_data.pop('profile', {})

        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        if password is not None:
            instance.set_password(password)
        instance.save()

        for (key, value) in profile_data.items():
            setattr(instance.profile, key, value)
        instance.profile.save()

        return instance