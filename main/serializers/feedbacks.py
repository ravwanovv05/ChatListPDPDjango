from rest_framework import serializers
from main.models.feedbacks import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
        read_only_fields = ('telegram_user_id',)


