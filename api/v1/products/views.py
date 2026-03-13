from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from app.utils.pagination import DefaultPagination
from apps.products.filters import ProductFilterSet
from apps.products.models import Product, Variation
from apps.products.serializers import ProductInventorySerializer, VariationSerializer


class ProductViewSet(GenericViewSet, ListModelMixin):
    pagination_class = DefaultPagination
    queryset = Product.objects.all()
    serializer_class = ProductInventorySerializer
    search_fields = ["name"]
    filterset_class = ProductFilterSet


class VariationViewSet(GenericViewSet, UpdateModelMixin):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer
