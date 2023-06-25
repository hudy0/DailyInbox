from django.db import models


class Entry(models.Model):
    """An entry store's the user's written for the day"""
    body = models.TextField()
    when = models.DateField()
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="entries")

    class Meta:
        verbose_name = 'entries'
        verbose_name_plural = 'entries'
