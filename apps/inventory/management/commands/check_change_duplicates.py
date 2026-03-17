from django.core.management.base import BaseCommand

from apps.inventory.models import Inventory, InventoryChange


class Command(BaseCommand):

    def handle(self, *args, **options):

        print("=" * 20)
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

            for index, c in enumerate(changes):
                if index != 0:
                    c.delete()

            print(item.product_variation, reference)
