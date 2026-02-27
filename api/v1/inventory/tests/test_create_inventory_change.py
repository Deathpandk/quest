from app.auth_token_testing import AuthTokenTesting
from apps.inventory.factories import InventoryFactory


class TestCreateInventoryChange(AuthTokenTesting):
    def setUp(self) -> None:
        self.inventory_1 = InventoryFactory()
        self.inventory_2 = InventoryFactory()

    def create_inventory_change(self, data, expected_status=201):
        return self.post("/api/v1/inventory/change/", data, expected_status)

    def test_list_inventory(self):
        response = self.create_inventory_change(
            [
                {
                    "product_variation_id": str(self.inventory_1.product_variation.id),
                    "change": -10,
                },
                {
                    "product_variation_id": str(self.inventory_2.product_variation.id),
                    "change": 10,
                },
            ]
        )

        self.inventory_1.refresh_from_db()
        self.assertEqual(self.inventory_1.quantity, -10)

        self.inventory_2.refresh_from_db()
        self.assertEqual(self.inventory_2.quantity, 10)
