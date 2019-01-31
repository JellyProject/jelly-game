from rest_framework import serializers
from .. import models


class SourceTechnologySerializer(serializers.ModelSerializer):
    child_technology = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    child_building = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = models.SourceTechnology
        fields = ('id', 'name', 'slug', 'version', 'era', 'description', 'cost', 'parent_technology',
                  'money_modifier', 'hydrocarbon_modifier', 'food_modifier', 'electricity_modifier',
                  'pollution_modifier', 'waste_modifier', 'economic_modifier', 'social_modifier',
                  'environmental_modifier', 'child_technology', 'child_building')