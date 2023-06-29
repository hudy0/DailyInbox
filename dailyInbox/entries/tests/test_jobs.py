from dailyInbox.entries.jobs import SendMailJob


class TestMailJob:
    def test_send_email(self):
        """An active account receive an email prompt"""
        job = SendMailJob()
        job.execute()
