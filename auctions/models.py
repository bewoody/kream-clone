from django.db import models
from core import models as core_models


class Auction(core_models.TimeStampedModel):

    """Auction Model Definition"""

    SIZE_CHOICES = [
        ("220", "220"),
        ("225", "225"),
        ("230", "230"),
        ("235", "235"),
        ("240", "240"),
        ("245", "245"),
        ("250", "250"),
        ("255", "255"),
        ("260", "260"),
        ("265", "265"),
        ("270", "270"),
        ("275", "275"),
        ("280", "280"),
        ("285", "285"),
        ("290", "290"),
        ("295", "295"),
        ("300", "300"),
        ("305", "305"),
        ("310", "310"),
        ("315", "315"),
        ("320", "320"),
    ]

    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="auctions"
    )
    size = models.CharField(max_length=3, choices=SIZE_CHOICES)


class Bidding(core_models.TimeStampedModel):
    """Bidding Model Definition"""

    ON_BIDDING = "ON_BIDDING"
    CONTRACTED = "CONTRACTED"

    STATUS_CHOICES = [(ON_BIDDING, "ON_BIDDING"), (CONTRACTED, "CONTRACTED")]

    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="biddings"
    )
    price = models.PositiveIntegerField()
