from rest_framework import serializers
from .. import models


class TechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Technology
        fields = '__all__'