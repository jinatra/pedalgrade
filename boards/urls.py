from django.urls import path

from boards.views import BoardCreateView, BoardReadView

urlpatterns = [
    path('', BoardCreateView.as_view()),
    path('/<int:board_id>', BoardReadView.as_view() )
]
