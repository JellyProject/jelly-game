from rest_framework import serializers

from ..models import Technology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Technology
