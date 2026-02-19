from django.db.models import IntegerChoices


class InventoryChangeTypeChoices(IntegerChoices):
    ADD = 1, "Agregar"
    REMOVE = -1, "Remover"
