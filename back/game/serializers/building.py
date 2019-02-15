from rest_framework import serializers
from .. import models


class BuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Building
        fields = '__all__'
