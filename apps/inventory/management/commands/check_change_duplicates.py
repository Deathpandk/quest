from django.core.management.base import BaseCommand

from apps.inventory.models import Inventory, InventoryChange


class Command(BaseCommand):

    def handle(self, *args, **options):

        for item in Inventory.objects.all():
            changes = InventoryChange.objects.filter(product_variation=item.product_variation)
            if len(changes) == 1:
                continue

            print("product variation: ", item.product_variation)
            print("changes", len(changes))

            for c in changes:
                print(c.created_at, c.change)
