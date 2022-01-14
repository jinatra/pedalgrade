from django.urls import path

from users.views import MailSubscribeView

urlpatterns = [
    path('/grade', MailSubscribeView.as_view()),
]
