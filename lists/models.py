from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):
    """List Model Definition"""

    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="list"
    )
    name = models.CharField(max_length=80)
    products = models.ManyToManyField("products.Size", related_name="lists", blank=True)

    def __str__(self) -> str:
        return self.name

    def count_products(self):
        return self.products.count()

    count_products.short_description = "Number of Products"
