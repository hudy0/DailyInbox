from dailyInbox.accounts.tests.factories import UserFactory, AccountFactory


class TestAccount:
    def test_factory(self):
        account = AccountFactory()
        assert account is not None
        assert account.user is not None
        assert account.status == account.Status.TRAILING


class TestUser:
    def test_factory(self):
        """the factory produces a valid instance"""
        user = UserFactory()
        assert user is not None
        assert user.account is not None

