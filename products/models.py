from django.db import models
from core.models import TimeStampedModel


class Brand(TimeStampedModel):
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name


class Photo(TimeStampedModel):
    image = models.ImageField(upload_to="products/%Y/%m/%d/")
    product = models.ForeignKey("Product", on_delete=models.CASCADE)


class Product(TimeStampedModel):

    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    name_en = models.CharField(max_length=120)
    name_kr = models.CharField(max_length=120)
    model_number = models.CharField(max_length=80)
    released = models.DateField()
    color = models.CharField(max_length=120)
    released_price = models.PositiveIntegerField()

    class Meta:
        verbose_name = "상품"
        verbose_name_plural = "상품"
        ordering = ["created", "updated"]

    def __str__(self) -> str:
        return f"{self.brand} - {self.name_kr}"
