from django.db import models

from app.models import NameModel, TimeStampedModel, UUIDModel


class Product(NameModel, UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=128)
