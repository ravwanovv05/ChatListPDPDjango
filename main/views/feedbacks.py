from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from main.models.feedbacks import Feedback
from main.serializers.feedbacks import FeedbackSerializer
from telegram_users.models.users import TelegramUser


class AddFeedbackView(GenericAPIView):
    serializer_class = FeedbackSerializer

    def get_queryset(self, *args, **kwargs):
        return Feedback.objects.all()

    def post(self, request, *args, **kwargs):
        data = self.get_serializer(data=request.data)
        data.is_valid(raise_exception=True)
        new_data = {
            'text': data.data['text'],
            'telegram_id': data.data['telegram_id'],
            'telegram_user_id': TelegramUser.objects.filter(telegram_id=int(data.data['telegram_id'])).first()
        }
        Feedback.objects.create(**new_data)
        return Response({'message': 'Successfully added feedback!'}, status.HTTP_201_CREATED)

