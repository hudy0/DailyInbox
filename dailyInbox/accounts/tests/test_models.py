from dailyInbox.accounts.models import Account
from dailyInbox.accounts.tests.factories import AccountFactory, UserFactory


class TestAccount:
    def test_factory(self):
        account = AccountFactory()
        assert account is not None
        assert account.user is not None
        assert account.status == account.Status.TRAILING

    def test_active(self):
        """the active manager method returns active accounts"""
        trailing = AccountFactory(status=Account.Status.TRAILING)
        active = AccountFactory(status=Account.Status.ACTIVE)
        exempt = AccountFactory(status=Account.Status.EXEMPT)
        AccountFactory(status=Account.Status.CANCELED)
        AccountFactory(status=Account.Status.TRIAL_EXPIRED)

        accounts = set(Account.objects.active())
        assert accounts == {trailing, active, exempt}


class TestUser:
    def test_factory(self):
        """the factory produces a valid instance"""
        user = UserFactory()
        assert user is not None
        assert user.account is not None
