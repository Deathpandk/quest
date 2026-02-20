from django.db import models

from app.models import TimeStampedModel, UUIDModel

from .catalogues import InventoryChangeTypeChoices


class Inventory(UUIDModel, TimeStampedModel):
    product = models.OneToOneField("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()


class InventoryChange(UUIDModel, TimeStampedModel):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    Type_of = InventoryChangeTypeChoices
    type_of = models.IntegerField(choices=Type_of)
    change = models.IntegerField()
