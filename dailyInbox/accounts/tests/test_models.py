from dailyInbox.accounts.tests.factories import UserFactory


class TestUser:
    def test_factory(self):
        """the factory produces a valid instance"""
        user = UserFactory()
        assert user is not None

