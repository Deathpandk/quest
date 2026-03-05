from rest_framework.routers import DefaultRouter

from .inventory.router import INVENTORY_ROUTER
from .products.router import PRODUCTS_ROUTER

API_V1_ROUTER = DefaultRouter()

API_V1_ROUTER.registry.extend(INVENTORY_ROUTER.registry)
API_V1_ROUTER.registry.extend(PRODUCTS_ROUTER.registry)
