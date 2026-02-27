from django.contrib import admin

from .models import Product, Variation


@admin.register(Product)
class Admin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Variation)
class Admin(admin.ModelAdmin):
    list_display = ["id", "product", "name"]
