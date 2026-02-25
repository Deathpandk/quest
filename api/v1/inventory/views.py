from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.inventory.models import Inventory
from apps.inventory.serializers import InventorySerializer


class InventoryViewSet(GenericViewSet, ListModelMixin):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
