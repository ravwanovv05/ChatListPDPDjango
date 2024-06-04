from rest_framework import serializers
from main.models.chats import Chat


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('name', 'link')
