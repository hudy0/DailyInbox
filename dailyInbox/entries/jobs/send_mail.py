from django.core import mail
from django.utils import timezone
from django_extensions.management.jobs import DailyJob

from dailyInbox.accounts.models import Account


class Job(DailyJob):
    help = "Send mail to active accounts"

    def execute(self):
        accounts = Account.objects.active()
        today = timezone.localdate()
        for account in accounts:
            mail.send_mail(
                # incorporate day of the week
                subject=f"It's {today:%A} {today:%b} {today:%-d}, 2023 how are you?",
                message="Replace this message",
                html_message="Replace this html message",
                from_email="Who is this from email",
                recipient_list=[account.user.email],
            )
