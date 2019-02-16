from rest_framework import serializers
from .. import models


class ResourcesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Resources
        fields = ('money',
                  'hydrocarbon')