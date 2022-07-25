from django.db import models
from core import models as core_models


class Brand(core_models.TimeStampedModel):
    name = models.CharField(max_length=40)


class Product(core_models.TimeStampedModel):

    """Product Model"""

    brand = models.ForeignKey(
        "Brand", on_delete=models.CASCADE, related_name="products"
    )
    name_en = models.CharField(max_length=120)
    name_kr = models.CharField(max_length=120)
    model_number = models.CharField(max_length=40, blank=True)
    released = models.DateField(null=True, blank=True)
    color = models.CharField(max_length=80, blank=True)
    released_price = models.PositiveIntegerField(blank=True)
