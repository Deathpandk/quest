from django.core.management.base import BaseCommand

from apps.inventory.models import Inventory, InventoryChange


class Command(BaseCommand):

    def handle(self, *args, **options):

        total_count = 0
        for item in Inventory.objects.all():
            changes = InventoryChange.objects.filter(product_variation=item.product_variation)

            if len(changes) == 1:
                continue

            reference = changes.first().change
            abort = False
            for c in changes:
                if c.change != reference:
                    abort = True

            if abort:
                continue

            total_count += 1
            print("=" * 20)
            print("product variation: ", item.product_variation)
            print("changes", len(changes))
            print("quantity: ", reference)

        print("Items totales: ", total_count)
