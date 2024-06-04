from django.urls import path

from main.views.chats import ChatListView
from main.views.feedbacks import AddFeedbackView

urlpatterns = [
    path('add-feedback', AddFeedbackView.as_view(), name='add_feedback'),
    path('chat-list', ChatListView.as_view(), name='chat_list')
]