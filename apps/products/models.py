from django.db import models

from app.utils.models import NameModel, TimeStampedModel, UUIDModel


class Product(NameModel, UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=256)
    keywords = models.TextField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ["order", "name"]


class Variation(NameModel, UUIDModel, TimeStampedModel):
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="variations"
    )
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.product.name} - {self.name}"
