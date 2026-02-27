from django.contrib import admin

from .models import Inventory, InventoryChange


@admin.register(Inventory)
class Admin(admin.ModelAdmin):
    list_display = ["product_variation__product", "product_variation", "quantity"]


@admin.register(InventoryChange)
class Admin(admin.ModelAdmin):
    list_display = ["product_variation__product", "product_variation", "change"]
