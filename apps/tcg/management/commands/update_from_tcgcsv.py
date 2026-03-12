from django.core.management.base import BaseCommand

from apps.tcg.utils.update_from_tcgcsv import update_game_products


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--game_id", type=int)

    def handle(self, *args, **options):
        game_id = options["game_id"]
        update_game_products(game_id)
