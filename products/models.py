from django.db import models
from core import models as core_models
from core.utils import upload_to


class AbstractItem(core_models.TimeStampedModel):

    """AbstractItem Model Definition"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name


class Category(AbstractItem):
    """Category Model Definition"""

    class Meta:
        verbose_name_plural = "Categories"


class Brand(AbstractItem):
    """Brand Model Definition"""

    pass


class Photo(core_models.TimeStampedModel):
    """Photo Model Definition"""

    image = models.ImageField(upload_to=upload_to("products", True))
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="photos"
    )


class Size(core_models.TimeStampedModel):
    """Size Model Definition"""

    size = models.CharField(max_length=20)
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="sizes"
    )


class Product(core_models.TimeStampedModel):

    """Product Model Definition"""

    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, related_name="products", null=True
    )
    brand = models.ForeignKey(
        "Brand", on_delete=models.CASCADE, related_name="products"
    )
    name_en = models.CharField(max_length=120)
    name_kr = models.CharField(max_length=120)
    model_number = models.CharField(max_length=40, blank=True)
    released = models.DateField(null=True, blank=True)
    color = models.CharField(max_length=80, blank=True)
    released_price = models.PositiveIntegerField(blank=True)
