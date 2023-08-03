from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Account
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(User, UserAdmin)


@admin.register(Account)
class AccountAdmin(SimpleHistoryAdmin):
    pass
