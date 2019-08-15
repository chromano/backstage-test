from django.conf import settings
from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status


class SumDifferenceTestCase(APITestCase):
    """
    Tests /sum_difference API endpoint.
    """

    def setUp(self):
        self.url = reverse('natural:sum_difference')

    def test_get_zero(self):
        response = self.client.get(self.url, {'n': 0})
        eq_(response.status_code, status.HTTP_200_OK)
        json_response = response.data
        try:
            eq_(json_response['value'], 0)
        except KeyError:
            self.fail('Unknown response: {}'.format(json_response))

    def test_get_positive(self):
        response = self.client.get(self.url, {'n': 10})
        eq_(response.status_code, status.HTTP_200_OK)
        json_response = response.data
        try:
            eq_(json_response['value'], 2640)
        except KeyError:
            self.fail('Unknown response: {}'.format(json_response))

    def test_get_negative(self):
        response = self.client.get(self.url, {'n': -10})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_missing_number(self):
        response = self.client.get(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_float(self):
        response = self.client.get(self.url, {'n': 3.14})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_str(self):
        response = self.client.get(self.url, {'n': '10'})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_not_number(self):
        response = self.client.get(self.url, {'n': 'a'})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_above_upper_bound(self):
        response = self.client.get(self.url, {
            'n': settings.CALC_NATURAL_SUM_DIFFERENCE_LIMIT + 1
        })
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_upper_bound(self):
        response = self.client.get(self.url, {
            'n': settings.CALC_NATURAL_SUM_DIFFERENCE_LIMIT
        })
        eq_(response.status_code, status.HTTP_200_OK)
