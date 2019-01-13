from rest_framework import serializers

from ..models import Balance


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Balance
