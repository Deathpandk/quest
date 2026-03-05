from app.utils.auth_token_testing import AuthTokenTesting
from apps.products.factories import VariationFactory


class TestListProducts(AuthTokenTesting):
    def setUp(self) -> None:
        VariationFactory()

    def list_products(self, expected_status=200):
        return self.get("/api/v1/products/", expected_status)

    def test_list_products(self):
        response = self.list_products()
        print(response)
        self.assertEqual(len(response.get("results")), 1)
