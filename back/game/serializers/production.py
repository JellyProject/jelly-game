from rest_framework import serializers
from .. import models


class ProductionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Production
        fields = ('money',
                  'hydrocarbon',
                  'food',
                  'electricity',
                  'pollution',
                  'waste')
