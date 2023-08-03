import sentry_sdk
from django.apps import AppConfig
from django.conf import settings
from sentry_sdk.integrations.django import DjangoIntegration
# from dailyInbox.sentry.dsn_config import SENTRY_DSN


def traces_sampler(sampling_context):
    """
    Select a sample rate off of the requested path.
    The root endpoint seemed to get hammered by some bot and ate a huge percent
    of transactions in a week. I don't care about that page right now,
    so ignore it.
    """
    path = sampling_context.get("wsgi_environ", {}).get("PATH_INFO", "")
    if path == "/":
        return 0
    return 1.0


class SentryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dailyInbox.sentry'

    def ready(self):
        """
        Initialize Sentry.
        Sentry initialization is moved to an application ready timeframe
        because it triggers circular imports with settings when used with
        type checking when django-stubs is enabled.
        """
        if not settings.SENTRY_ENABLED:
            return

    sentry_sdk.init(
        dsn="https://f731863cf6ad44bbb7cd4e1e2713d871@o4505600011534336.ingest.sentry.io/4505600022151168",
        integrations=[DjangoIntegration()],
        traces_sampler=traces_sampler,
        send_default_pii=True,
    )
