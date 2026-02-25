import factory

from apps.products.factories import ProductFactory


class InventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "inventory.Inventory"

    product = factory.SubFactory(ProductFactory)
    quantity = 3
