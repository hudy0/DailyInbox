from email_service.accounts.tests.factories import UserFactory


class TestUser:
    def test_factory(self):
        user = UserFactory()

        assert user is not None
