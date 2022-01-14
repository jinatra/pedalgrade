from django.urls import path

from users.views import MailSubscribeView

urlpatterns = [
    path('/signin', MailSubscribeView.as_view()),
]
