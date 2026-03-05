from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from app.utils.pagination import DefaultPagination
from apps.products.filters import ProductFilterSet
from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductViewSet(GenericViewSet, ListModelMixin):
    pagination_class = DefaultPagination
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ["name"]
    filterset_class = ProductFilterSet
