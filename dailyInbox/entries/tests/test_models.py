from dailyInbox.entries.tests.factories import EntryFactory


class TestEntry:
    def test_factory(self):
        """the factory produces a valid dailyInbox"""
        entry = EntryFactory()

        assert entry.body != ""
        assert entry.when is not None
        assert entry.user is not None
