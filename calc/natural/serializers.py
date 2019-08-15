from django.conf import settings
from rest_framework import serializers

from .models import SumDifference


class SumDifferenceRequestSerializer(serializers.Serializer):
    n = serializers.IntegerField(
        min_value=0, max_value=settings.CALC_NATURAL_SUM_DIFFERENCE_LIMIT)


class SumDifferenceResponseSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='solution')

    class Meta:
        model = SumDifference
        fields = (
            'datetime',
            'occurrences',
            'number',
            'value',
        )
