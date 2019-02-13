from rest_framework import serializers
from .. import models


class BalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Balance
        fields = ('economic',
                  'social',
                  'environmental')
