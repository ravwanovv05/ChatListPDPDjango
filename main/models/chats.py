from django.db import models


class Chat(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Name')
    link = models.CharField(max_length=200, verbose_name='Link')
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'

    def __str__(self):
        return f'{self.name} | {self.pk}'



