from rest_framework import serializers

from .models import Product, Variation


class VariationInventorySerializer(serializers.ModelSerializer):
    inventory = serializers.IntegerField(source="inventory.quantity")

    class Meta:
        model = Variation
        fields = ["id", "name", "price", "inventory"]


class ProductInventorySerializer(serializers.ModelSerializer):
    variations = VariationInventorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "order", "variations"]


class VariationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variation
        fields = ["id", "name", "price"]
        read_only_fields = ["id"]
