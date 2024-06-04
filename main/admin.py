from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from main.models.chats import Chat
from main.models.feedbacks import Feedback
from main.resources import ChatResource, FeedbackResource


@admin.register(Chat)
class ChatAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name', 'link')
    list_per_page = 15
    resource_class = ChatResource


@admin.register(Feedback)
class FeedbackAdmin(ImportExportModelAdmin):
    list_display = ('id', 'telegram_id', 'telegram_user_id')
    list_display_links = ('id',)
    list_per_page = 15
    resource_class = FeedbackResource

