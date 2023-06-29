from django_extensions.management.jobs import DailyJob


class SendMailJob(DailyJob):
    help = "Send mail to active accounts"

    def execute(self):
        pass
