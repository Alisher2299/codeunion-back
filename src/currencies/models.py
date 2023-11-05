from django.db import models

from common.models.abstract import TimeStampedModel


class Currency(TimeStampedModel):
    name = models.CharField(max_length=3, default="")
    rate = models.FloatField(default=00.00, blank=True, )

    def __str__(self):
        return f"{self.name}|{self.rate}"
