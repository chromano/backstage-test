from django.conf import settings
from django.core import validators
from django.db import models


class SumDifference(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    number = models.IntegerField(validators=[
        validators.MinValueValidator(0),
        validators.MaxValueValidator(settings.CALC_NATURAL_SUM_DIFFERENCE_LIMIT)
    ])
    solution = models.IntegerField()
    occurrences = models.IntegerField(default=1)

    class Meta:
        ordering = ['-datetime']
