from uuid import uuid4

from django.db import models


class UUIDModel(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class NameModel:
    name: models.CharField

    def __str__(self):
        return self.name
