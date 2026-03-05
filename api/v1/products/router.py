from rest_framework.routers import SimpleRouter

from .views import ProductViewSet

PRODUCTS_ROUTER = SimpleRouter()

PRODUCTS_ROUTER.register("products", ProductViewSet, basename="products")
