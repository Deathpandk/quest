import factory

from apps.products.factories import VariationFactory


class InventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "inventory.Inventory"

    product_variation = factory.SubFactory(VariationFactory)
    quantity = 0
