from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    pass


class Account(models.Model):
    """Account holds the users state"""

    class Status(models.IntegerChoices):
        EXEMPT = 1
        ACTIVE = 2
        TRAILING = 3
        CANCELED = 4
        TRIAL_EXPIRED = 5

    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status.choices, default=Status.TRAILING, db_index=True)


@receiver(post_save, sender=User)
def create_account(instance, sender, created, **keywords):
    """A new user gets an associated account"""
    if created:
        Account.objects.create(user=instance)
