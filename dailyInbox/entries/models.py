from __future__ import annotations

import random

from django.contrib.auth.models import User
from django.db import models


class EntryManager(models.Manager):
    """A manager to provide custom methods for entry"""

    def get_random_for(self, user: User) -> Entry | None:
        queryset = self.get_queryset().filter(user=user)
        count = queryset.count()
        if count == 0:
            return None
        index = random.choice(range(0, count))
        return queryset[index]


class Entry(models.Model):
    """An entry store's the user's written for the day"""

    body = models.TextField()
    when = models.DateField()
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="entries",
    )
    objects = EntryManager()

    class Meta:
        verbose_name = "entries"
        verbose_name_plural = "entries"
