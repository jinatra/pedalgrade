from django.urls import path

from boards.views import BoardCreateView, BoardReadView, MainPageView

urlpatterns = [
    path('', BoardCreateView.as_view()),
    path('/<int:board_id>', BoardReadView.as_view()),
    path('/list', MainPageView.as_view()),
]
