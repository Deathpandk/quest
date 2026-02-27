from django.db import models

from app.models import NameModel, TimeStampedModel, UUIDModel


class Product(NameModel, UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=128)


class Variation(NameModel, UUIDModel, TimeStampedModel):
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="variations"
    )
    name = models.CharField(max_length=128)
