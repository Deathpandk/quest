from django.db import models

from app.models import TimeStampedModel, UUIDModel


class Inventory(UUIDModel, TimeStampedModel):
    product = models.OneToOneField("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()


class InventoryChange(UUIDModel, TimeStampedModel):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    change = models.IntegerField()

    def apply(self):
        self.product.inventory.quantity += self.change
        return self.product.inventory
