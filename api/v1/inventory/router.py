from rest_framework.routers import SimpleRouter

from .views import InventoryViewSet

INVENTORY_ROUTER = SimpleRouter()

INVENTORY_ROUTER.register("inventory", InventoryViewSet, basename="inventory")
