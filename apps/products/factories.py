import factory


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "products.Product"

    name = factory.Sequence(lambda n: f"Product {n + 1}")


class VariationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "products.Variation"

    product = factory.SubFactory(ProductFactory)
    name = factory.Sequence(lambda n: f"Variation {n + 1}")
