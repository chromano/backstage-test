from django.db.models import F
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import SumDifference
from .serializers import SumDifferenceRequestSerializer, \
    SumDifferenceResponseSerializer
from .services import calc_sum_difference


def _create_sum_difference(n):
    req_serialization = SumDifferenceRequestSerializer(data={'n': n})
    req_serialization.is_valid(raise_exception=True)

    solution = calc_sum_difference(req_serialization.data['n'])

    sum_difference, created = SumDifference.objects.get_or_create(
        number=req_serialization.data['n'], solution=solution)
    if not created:
        sum_difference.occurrences = F('occurrences') + 1
        sum_difference.save(update_fields=['occurrences'])

    result = SumDifferenceResponseSerializer(sum_difference)

    return result.data


def _list_sum_differences():
    sum_differences = SumDifference.objects.all()
    result = SumDifferenceResponseSerializer(sum_differences, many=True)

    return Response(result.data)


@api_view(['GET'])
def sum_difference(request):
    if 'n' in request.query_params:
        return _create_sum_difference(request.query_params['n'])

    return _list_sum_differences()