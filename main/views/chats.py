from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from main.models.chats import Chat
from main.serializers.chats import ChatSerializer


class ChatListView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
