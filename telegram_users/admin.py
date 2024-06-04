from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from telegram_users.models.users import TelegramUser
from telegram_users.resources import TelegramUserResource


@admin.register(TelegramUser)
class TelegramUserAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'joined_at')
    list_display_links = ('id',)
    search_fields = ('first_name', 'last_name')
    list_per_page = 15
    resource_class = TelegramUserResource

