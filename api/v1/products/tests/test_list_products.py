from app.utils.auth_token_testing import AuthTokenTesting
from apps.products.factories import VariationFactory


class TestListProducts(AuthTokenTesting):
    def setUp(self) -> None:
        self.variation = VariationFactory()

    def list_products(self, params=None, expected_status=200):
        return self.get("/api/v1/products/", expected_status, params=params)

    def test_list_products(self):
        response = self.list_products()
        self.assertEqual(len(response.get("results")), 1)
        self.assertEqual(response.get("results")[0].get("id"), str(self.variation.product.id))

    def test_list_products_filter_from_number(self):
        variation_2 = VariationFactory(product__order=3)
        response = self.list_products(params={"from_number": 3})
        self.assertEqual(len(response.get("results")), 1)
        self.assertEqual(response.get("results")[0].get("id"), str(variation_2.product.id))
