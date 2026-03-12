import requests

from apps.tcg.models import Expansion, ExpansionProduct, Game, Rarity, Version

BASE_URL = "https://tcgcsv.com/tcgplayer"


def update_game_products(game_id):
    game = Game.objects.get(
        tcgcsv_id=game_id,
    )

    groups_response = requests.get(f"{BASE_URL}/{game_id}/groups")
    groups = groups_response.json().get("results")

    expansions = []
    for group in groups:
        expansion, _ = Expansion.objects.get_or_create(
            tcgcsv_id=group.get("groupId"),
            defaults={
                "game": game,
                "name": group.get("name"),
                "release_date": group.get("publishedOn")[:10],
            },
        )
        expansions.append(expansion)

    log_count = 0
    for expansion in expansions:
        log_count += 1
        group_id = expansion.tcgcsv_id
        print(f"Processing Expansion: {expansion.name} {log_count}/{len(expansions)}")
        response = requests.get(f"{BASE_URL}/{game_id}/{group_id}/products")
        cards = response.json().get("results")
        card_instances = {}
        expansion_cards = None
        for card in cards:
            name = card.get("name")
            if "-" in name:
                name_parts = name.split("-")
                last_part = name_parts[-1]
                if any([char.isnumeric() for char in last_part]):
                    name = "-".join(name_parts[:-1])
                    name = name.strip()
            data = card.get("extendedData")
            data = {item.get("name"): item.get("value") for item in data} if data else None
            card_image_url = card.get("imageUrl")
            defaults = {
                "game": game,
                "expansion": expansion,
                "name": name,
                "image_url": card_image_url,
            }

            # If extended data has Number consider parse it and consider it a single
            if data and data.get("Number"):
                number, exp_number = _parse_number(game, data.get("Number"))
                if number:
                    defaults["number"] = number
                    defaults["type_of"] = ExpansionProduct.SINGLES
                if exp_number:
                    expansion_cards = exp_number

            # Pokemon qr codes, just mark as single
            elif "Code Card" in name:
                defaults["type_of"] = ExpansionProduct.SINGLES
            else:
                defaults["type_of"] = ExpansionProduct.SEALED_PRODUCT

            # If there is Rarity data parse it and use it
            if data and data.get("Rarity"):
                rarity, _ = Rarity.objects.get_or_create(
                    game=game,
                    name=data.get("Rarity"),
                    defaults={
                        "tcgcsv_name": data.get("Rarity"),
                    },
                )
                defaults["rarity"] = rarity
                del data["Rarity"]

            # Save extended data on DB
            if data:
                defaults["data"] = data

            card_data_id = card.get("productId")
            card, new = ExpansionProduct.objects.get_or_create(
                expansion=expansion,
                game=game,
                tcgcsv_id=card_data_id,
                defaults=defaults,
            )

            # Update image if not present on existent card
            if not new:
                for key, value in defaults.items():
                    setattr(card, key, value)
                if card.image_file is None:
                    card.default_small_image_url = card_image_url
                    card.image_default_url = card_image_url
                card.save()

            card_instances[str(card.tcgcsv_id)] = card
        if expansion_cards:
            print("set count as:", expansion_cards)
            expansion.cards_count = expansion_cards
            expansion.save()
        prices_response = requests.get(f"{BASE_URL}/{game_id}/{group_id}/prices")
        prices = prices_response.json().get("results")

        versions = {}
        for price in prices:
            card_id = price.get("productId")
            version_code = price.get("subTypeName")

            version = versions.get(version_code, None)
            if version is None:
                version, _ = Version.objects.get_or_create(
                    game=game,
                    tcgcsv_name=version_code,
                    defaults={
                        "name": version_code,
                    },
                )
            card = card_instances.get(str(card_id))
            if card:
                card.versions.add(version)
            else:
                print(f"Error: Failed to add version {version_code} to {card_id}")


def _parse_number(game, number_value):
    number, exp_number = None, None

    # Special parse for One Piece (68) and Digimon (63)
    if game.tcgcsv_id in [63, 68]:
        number_split = number_value.split("-")
        if len(number_split) == 2:
            number_part = number_split[1]
            number_numeric = [char for char in number_part if char.isnumeric()]
            number = "".join(number_numeric)
    else:
        number_split = number_value.split("/")
        number_part = number_split[0]

        number_numeric = [char for char in number_part if char.isnumeric()]
        if number_numeric:
            number = "".join(number_numeric)

        if len(number_split) == 2:
            exp_number_part = number_split[1]
            exp_number_numeric = [char for char in exp_number_part if char.isnumeric()]
            if exp_number_numeric:
                exp_number = "".join(exp_number_numeric)

    return number, exp_number
