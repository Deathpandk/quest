from rest_framework.routers import SimpleRouter

from .views import ProductViewSet, VariationViewSet

PRODUCTS_ROUTER = SimpleRouter()

PRODUCTS_ROUTER.register("products", ProductViewSet, basename="products")
PRODUCTS_ROUTER.register("variations", VariationViewSet, basename="variations")
