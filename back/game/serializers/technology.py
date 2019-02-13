from rest_framework import serializers
from .. import models


class TechnologySerializer(serializers.ModelSerializer):
    unlocked = serializers.BooleanField(read_only=True)

    class Meta:
        model = models.Technology
        fields = ('unlocked', 'slug', 'purchased', 'state')
