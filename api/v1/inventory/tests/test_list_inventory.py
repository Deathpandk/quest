from app.auth_token_testing import AuthTokenTesting
from apps.inventory.factories import InventoryFactory
from apps.products.factories import VariationFactory


class TestListInventory(AuthTokenTesting):
    def setUp(self) -> None:
        InventoryFactory()
        VariationFactory()

    def list_inventory(self, expected_status=200):
        return self.get("/api/v1/inventory/", expected_status)

    def test_list_inventory(self):
        response = self.list_inventory()

        self.assertEqual(len(response), 1)
