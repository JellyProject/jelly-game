from rest_framework import serializers
from .. import models


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Technology
        fields = ('unlocked', 'source', 'purchased', 'state')
        read_only_fields = ('unlocked', 'source', 'state')

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