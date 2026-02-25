from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.inventory.models import Inventory, InventoryChange
from apps.inventory.serializers import InventorySerializer


class InventoryViewSet(GenericViewSet, ListModelMixin):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    @action(methods=["post"], detail=False, url_path="change")
    def create_inventory_change(self, request):
        inventory_changes = request.data

        change_objects, updated_inventories = [], []
        for change in inventory_changes:
            change_objects.append(
                InventoryChange(
                    product_id=change.get("product_uuid"),
                    change=change.get("change"),
                )
            )

        change_objects = InventoryChange.objects.bulk_create(change_objects)

        Inventory.objects.bulk_update(
            [change.apply() for change in change_objects], fields=["quantity"]
        )
        return Response(status=status.HTTP_201_CREATED)
