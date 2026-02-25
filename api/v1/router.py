from rest_framework.routers import DefaultRouter

from .inventory.router import INVENTORY_ROUTER

API_V1_ROUTER = DefaultRouter()

API_V1_ROUTER.registry.extend(INVENTORY_ROUTER.registry)
