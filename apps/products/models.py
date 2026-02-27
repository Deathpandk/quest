from django.db import models

from app.utils.models import NameModel, TimeStampedModel, UUIDModel


class Product(NameModel, UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ["name"]


class Variation(NameModel, UUIDModel, TimeStampedModel):
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="variations"
    )
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.product.name} - {self.name}"
