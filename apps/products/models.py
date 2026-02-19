from django.db import models

from app.models import NameModel, TimeStampedModel, UUIDModel


class Product(UUIDModel, TimeStampedModel, NameModel):
    name = models.CharField(max_length=128)
