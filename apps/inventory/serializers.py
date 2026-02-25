from rest_framework import serializers

from apps.products.serializers import ProductSerializer

from .models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Inventory
        fields = ["uuid", "product", "quantity"]
