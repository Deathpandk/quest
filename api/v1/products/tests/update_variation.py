from app.utils.auth_token_testing import AuthTokenTesting
from apps.products.factories import VariationFactory


class TestListProducts(AuthTokenTesting):
    def setUp(self) -> None:
        self.variation = VariationFactory()

    def update_variation(self, id, data, expected_status=200):
        return self.patch(f"/api/v1/variations/{id}", data, expected_status)

    def test_update_variation(self):
        price = 1234.56
        self.update_variation(
            self.variation.id,
            {
                "price": price,
            },
        )

        self.variation.refresh_from_db()
        self.assertEqual(self.variation.price, price)
