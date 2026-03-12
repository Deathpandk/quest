from django.core.management.base import BaseCommand

from apps.products.models import Product, Variation
from apps.tcg.models import ExpansionProduct, Game, TCGProduct, TCGVariation


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--game_id", type=int)

    def handle(self, *args, **options):
        game_id = options["game_id"]

        game = Game.objects.get(tcgcsv_id=game_id)

        # Focus in singles for now
        game_objects = ExpansionProduct.objects.filter(
            game_id=game.id, type_of=ExpansionProduct.SINGLES
        )

        for item in game_objects:

            keywords = f"EXP:{item.expansion.name}"
            product_name = f"{item.expansion.name} - {item.name}"
            product_order = item.number

            if hasattr(item, "tcgproduct"):
                tcg_product = item.tcgproduct
                product = tcg_product.product
                if product.name != product_name or product.order != product_order:
                    product.order = product_order
                    product.name = product_name
                    product.save()
            else:
                product = Product.objects.create(
                    name=product_name,
                    keywords=keywords,
                )
                tcg_product = TCGProduct.objects.create(
                    expansion_product=item,
                    product=product,
                )

            for version in item.versions.all():

                variation_name = version.name

                tcg_variation = tcg_product.variations.filter(version=version).first()
                if tcg_variation:
                    variation = tcg_variation.variation
                    if variation.name != variation_name:
                        variation.name = variation_name
                        variation.save()
                else:
                    variation = Variation.objects.create(
                        product=product,
                        name=version.name,
                    )
                    TCGVariation.objects.create(
                        tcg_product=tcg_product,
                        version=version,
                        variation=variation,
                    )
