from django.core.management.base import BaseCommand

from apps.inventory.models import Inventory, InventoryChange


class Command(BaseCommand):

    def handle(self, *args, **options):

        for item in Inventory.objects.all():
            changes = InventoryChange.objects.filter(product_variation=item.product_variation)
            inventory = 0
            for change in changes:
                inventory += change.change
            item.quantity = inventory
            item.save()
