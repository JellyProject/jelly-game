from rest_framework import serializers
from .. import models


class BuildingSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(source='source.slug', required=False)

    class Meta:
        model = models.Building
        fields = ('unlocked', 'slug', 'copies', 'state', 'quantity_cap')
        read_only_fields = ('unlocked', 'slug', 'state', 'quantity_cap')
