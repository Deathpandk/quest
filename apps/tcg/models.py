from django.db import models

from app.utils.models import NameModel, UUIDModel


class Game(NameModel, UUIDModel):
    name = models.CharField(max_length=64)
    tcgcsv_id = models.CharField(max_length=20)


class Expansion(NameModel, UUIDModel):
    game = models.ForeignKey("tcg.Game", on_delete=models.PROTECT)
    name = models.CharField(max_length=64)
    release_date = models.DateField(null=True, blank=True)
    tcgcsv_id = models.CharField(max_length=20)


class Version(NameModel, UUIDModel):
    game = models.ForeignKey("tcg.Game", on_delete=models.PROTECT)

    tcgcsv_name = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.game.name}: {self.name}"


class Rarity(NameModel, UUIDModel):
    game = models.ForeignKey("tcg.Game", on_delete=models.PROTECT)

    tcgcsv_name = models.CharField(max_length=40)
    name = models.CharField(max_length=64)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["game", "order"]


class ExpansionProduct(NameModel, UUIDModel):
    tcgcsv_id = models.CharField(max_length=20, null=True, blank=True)
    game = models.ForeignKey("tcg.Game", on_delete=models.PROTECT)
    expansion = models.ForeignKey("tcg.Expansion", on_delete=models.PROTECT, null=True, blank=True)
    rarity = models.ForeignKey("tcg.Rarity", on_delete=models.PROTECT, null=True, blank=True)

    number = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=256)

    data = models.JSONField(null=True, blank=True)

    image_url = models.URLField(null=True, blank=True)

    versions = models.ManyToManyField("tcg.Version", blank=True)

    SINGLES = "SIN"
    SEALED_PRODUCT = "SEA"
    TYPE_OPTIONS = ((SINGLES, "Cartas Sueltas"), (SEALED_PRODUCT, "Producto Cerrado"))
    type_of = models.CharField(max_length=3, choices=TYPE_OPTIONS, default=SINGLES)

    class Meta:
        ordering = ["type_of", "game", "expansion", "number"]


class TCGProduct(UUIDModel):
    expansion_product = models.OneToOneField(
        "tcg.ExpansionProduct", on_delete=models.PROTECT, related_name="tcgproduct"
    )
    product = models.OneToOneField(
        "products.Product", on_delete=models.PROTECT, related_name="tcgproduct"
    )


class TCGVariation(UUIDModel):
    tcg_product = models.ForeignKey(
        "tcg.TCGProduct", on_delete=models.PROTECT, related_name="variations"
    )
    version = models.ForeignKey("tcg.Version", on_delete=models.PROTECT)
    variation = models.OneToOneField(
        "products.Variation", on_delete=models.PROTECT, related_name="tcgproduct"
    )
