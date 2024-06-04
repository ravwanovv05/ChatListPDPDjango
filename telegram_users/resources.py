from import_export import resources
from telegram_users.models.users import TelegramUser


class TelegramUserResource(resources.ModelResource):
    class Meta:
        model = TelegramUser
