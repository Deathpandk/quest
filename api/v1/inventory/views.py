from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from app.utils.pagination import DefaultPagination
from apps.inventory.models import Inventory, InventoryChange
from apps.products.models import Product
from apps.products.serializers import ProductInventorySerializer

from .schemas import CreateInventoryChangeRequest


class InventoryViewSet(GenericViewSet, ListModelMixin):
    pagination_class = DefaultPagination
    queryset = Product.objects.filter(variations__inventory__isnull=False).prefetch_related(
        "variations", "variations__inventory"
    )
    serializer_class = ProductInventorySerializer
    search_fields = ["name"]

    @action(methods=["post"], detail=False, url_path="change")
    def create_inventory_change(self, request):
        inventory_changes = [CreateInventoryChangeRequest(**item) for item in request.data]

        change_objects, updated_inventories = [], []
        for change in inventory_changes:
            change_objects.append(
                InventoryChange(
                    product_variation_id=change.product_variation_id,
                    change=change.change,
                )
            )

        change_objects = InventoryChange.objects.bulk_create(change_objects)

        Inventory.objects.bulk_update(
            [change.apply() for change in change_objects], fields=["quantity"]
        )
        return Response(status=status.HTTP_201_CREATED)
