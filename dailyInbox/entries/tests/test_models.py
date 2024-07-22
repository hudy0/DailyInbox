from dailyInbox.accounts.tests.factories import UserFactory
from dailyInbox.entries.models import Entry
from dailyInbox.entries.tests.factories import EntryFactory


class TestEntry:
    def test_factory(self):
        """the factory produces a valid dailyInbox"""
        entry = EntryFactory()

        assert entry.body != ""
        assert entry.when is not None
        assert entry.user is not None

    def test_get_random_for(self):
        """The get_random_for method, can get random entries"""
        user = UserFactory()
        entry_1 = EntryFactory(user=user)
        entry_2 = EntryFactory(user=user)
        entry = Entry.objects.get_random_for(user)
        assert entry in {entry_1, entry_2}

    def test_get_random_for_only_user(self):
        """the get_random_for only user method, belongs to the user"""
        entry_1 = EntryFactory()
        EntryFactory()
        entry = Entry.objects.get_random_for(entry_1.user)
        assert entry == entry_1

    def test_get_random_for_no_entries(self):
        """No entries are returned when they are np entries to pick up"""
        user = UserFactory()
        entry = Entry.objects.get_random_for(user)
        assert entry is None
