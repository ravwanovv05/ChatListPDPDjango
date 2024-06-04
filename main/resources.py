from import_export import resources
from main.models.chats import Chat
from main.models.feedbacks import Feedback


class ChatResource(resources.ModelResource):
    class Meta:
        model = Chat


class FeedbackResource(resources.ModelResource):
    class Meta:
        model = Feedback
