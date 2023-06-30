from django.core import mail
from django_extensions.management.jobs import DailyJob

from dailyInbox.accounts.models import Account


class Job(DailyJob):
    help = "Send mail to active accounts"

    def execute(self):
        accounts = Account.objects.active()
        for account in accounts:
            mail.send_mail(subject="Replace this subject",
                           message="Replace this message",
                           html_message="Replace this html message",
                           from_email="Who is this from email",
                           recipient_list=[account.user.email],
                           )
