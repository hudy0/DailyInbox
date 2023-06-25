from django.contrib import admin

from dailyInbox.entries.models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    raw_id_fields = ("user", )
    list_display = ("id", "user", "when", )
    list_filter = ("when", )
