from django.db import models

from app.utils.models import TimeStampedModel, UUIDModel


class Inventory(UUIDModel, TimeStampedModel):
    product_variation = models.OneToOneField(
        "products.Variation", on_delete=models.CASCADE, related_name="inventory"
    )
    quantity = models.IntegerField()


class InventoryChange(UUIDModel, TimeStampedModel):
    product_variation = models.ForeignKey(
        "products.Variation", on_delete=models.CASCADE, related_name="inventory_changes"
    )
    change = models.IntegerField()

    def apply(self):
        if hasattr(self.product_variation, "inventory"):
            self.product_variation.inventory.quantity += self.change
        else:
            Inventory.objects.create(product_variation=self.product_variation, quantity=self.change)
        return self.product_variation.inventory
