from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    motto = serializers.CharField(allow_blank=True, required=False)
    image = serializers.SerializerMethodField()    # Linked to get_image
    players = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('username', 'motto', 'image', 'players')
        read_only_fields = ('username',)

    def get_image(self, obj):
        if obj.image:
            return obj.image
        return 'https://static.productionready.io/images/smiley-cyrus.jpg'
