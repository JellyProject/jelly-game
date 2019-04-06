from rest_framework import serializers
from .. import models
from .source_technology import SourceTechnologySerializer


class TechnologySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(source='source.slug', required=False)

    class Meta:
        model = models.Technology
        fields = ('unlocked', 'slug', 'purchased', 'state')
        read_only_fields = ('unlocked', 'slug', 'state')

    def validate(self, data):
        """
        Check if data has a (purchased, True) key-value pair.
        """
        purchased = data.get('purchased', None)

        if purchased is None:
            raise serializers.ValidationError(
                '"purchased" field missing.'
            )

        if not purchased:
            raise serializers.ValidationError(
                '"purchased" should be true.'
            )

        return {
            'purchased': purchased,
        }

    def update(self, instance, validated_data):
        """ Purchase a technology. """
        setattr(instance, "purchased", validated_data["purchased"])
        instance.save()
        return instance