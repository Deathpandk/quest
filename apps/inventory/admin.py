from django.contrib import admin

from .models import Inventory, InventoryChange


@admin.register(Inventory)
class Admin(admin.ModelAdmin):
    list_display = ["product", "quantity"]


@admin.register(InventoryChange)
class Admin(admin.ModelAdmin):
    list_display = ["product", "type_of", "change"]
