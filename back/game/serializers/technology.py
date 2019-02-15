from rest_framework import serializers
from .. import models


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Technology
        fields = ('unlocked', 'slug', 'purchased', 'state')
        read_only_fields = ('unlocked', 'slug', 'state')

    def validate(self, data):
        """
        Check if purchased is valid, and return the current instance.

        validate() should only be used for updates.
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