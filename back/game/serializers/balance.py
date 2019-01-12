from rest_framework import serializers

from ..models import Balance


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = Balance
