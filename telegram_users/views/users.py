from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from telegram_users.models.users import TelegramUser
from telegram_users.serializers.users import TelegramUserSerializer


class AddTelegramUserView(GenericAPIView):
    serializer_class = TelegramUserSerializer

    def get_queryset(self, *args, **kwargs):
        return TelegramUser.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Successfully added telegram user!'}, status=status.HTTP_201_CREATED)


