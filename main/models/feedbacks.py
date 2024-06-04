from django.db import models

from telegram_users.models.users import TelegramUser


class Feedback(models.Model):
    text = models.TextField(verbose_name='Text')
    telegram_id = models.PositiveBigIntegerField(verbose_name='Telegram ID')
    telegram_user_id = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name='Telegram user ID')

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return self.text
