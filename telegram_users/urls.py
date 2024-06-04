from django.urls import path
from telegram_users.views.users import AddTelegramUserView

urlpatterns = [
    path('add-user', AddTelegramUserView.as_view(), name='add_user'),

]
