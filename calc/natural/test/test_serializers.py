from django.conf import settings
from django.test import TestCase
from nose.tools import eq_, ok_

from ..models import SumDifference
from ..serializers import SumDifferenceRequestSerializer, \
    SumDifferenceResponseSerializer


class SumDifferenceResponseSerializerTestCase(TestCase):
    def test_structure(self):
        sum_difference = SumDifference(
            occurrences=1,
            number=10,
            solution=2640,
        )
        sum_difference.save()
        sum_difference.datetime = sum_difference.datetime.replace(tzinfo=None)
        serializer = SumDifferenceResponseSerializer(sum_difference)
        data = serializer.data
        eq_(data, {
            'datetime': sum_difference.datetime.isoformat(timespec='microseconds') + 'Z',
            'occurrences': sum_difference.occurrences,
            'number': sum_difference.number,
            'value': sum_difference.solution
        })


class SumDifferenceRequestSerializerTestCase(TestCase):
    def test_serialize_empty_data(self):
        serializer = SumDifferenceRequestSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serialize_valid_data(self):
        serializer = SumDifferenceRequestSerializer(data={'n': 10})
        ok_(serializer.is_valid())

    def test_serialize_invalid_data(self):
        serializer = SumDifferenceRequestSerializer(data={'n': 'a'})
        eq_(serializer.is_valid(), False)

        serializer = SumDifferenceRequestSerializer(data={'n': 3.10})
        eq_(serializer.is_valid(), False)

        serializer = SumDifferenceRequestSerializer(data={'n': -10})
        eq_(serializer.is_valid(), False)

        serializer = SumDifferenceRequestSerializer(data={
            'n': settings.CALC_NATURAL_SUM_DIFFERENCE_LIMIT + 1
        })
        eq_(serializer.is_valid(), False)
