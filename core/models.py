from django.db import models


class TimeStampedModle(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
