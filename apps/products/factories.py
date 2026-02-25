import factory


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "products.Product"

    name = factory.Sequence(lambda n: f"Product {n + 1}")
