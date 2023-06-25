from dailyInbox.entries.tests.factories import EntriesFactory


class TestEntry:
    def test_factory(self):
        """the factory produces a valid dailyInbox"""
        entry = EntriesFactory()

        assert entry.body != ""
        assert entry.when is not None
        assert entry.user is not None
