from django.apps import AppConfig
from anymail.signals import inbound

from dailyInbox.entries.recivers import handle_inbound


class EntriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dailyInbox.entries'

    def ready(self):
        inbound.connect(handle_inbound)
