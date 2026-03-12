import json

from django.contrib import admin
from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JsonLexer

from .models import (
    Expansion,
    ExpansionProduct,
    Game,
    Rarity,
    Version,
)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ["id", "game", "name", "order"]
    search_fields = ["name"]
    list_filter = ["game"]


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "tcgcsv_id",
    ]
    search_fields = ["name"]


@admin.register(Rarity)
class RarityAdmin(admin.ModelAdmin):
    list_display = ["id", "game", "order", "name"]
    list_filter = ["game"]
    search_fields = ["name"]


@admin.register(ExpansionProduct)
class ExpProdAdmin(admin.ModelAdmin):
    list_display = ["id", "expansion", "number", "name"]
    fields = [
        "pk",
        "tcgcsv_id",
        "game",
        "expansion",
        "rarity",
        "number",
        "name",
        "image_url",
        "type_of",
        "versions",
        "extra_data",
    ]
    readonly_fields = ["pk", "extra_data"]
    list_filter = ("game",)
    search_fields = ["name", "tcgcsv_id"]

    def extra_data(self, instance):
        """Function to display pretty version of our data"""
        response = json.dumps(instance.data, sort_keys=False, indent=4)
        formatter = HtmlFormatter()
        response = highlight(response, JsonLexer(), formatter)
        style = "<style>" + formatter.get_style_defs() + "</style><br>"
        return mark_safe(style + response)


@admin.register(Expansion)
class ExpansionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "tcgcsv_id",
        "name",
    ]
    list_filter = [
        "game",
        ("tcgcsv_id", admin.EmptyFieldListFilter),
    ]
    search_fields = ["name"]
