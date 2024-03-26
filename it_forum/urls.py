from django.urls import path
from it_forum.views import (AnswerCreateView,
                            AnswersListView,
                            AnswerDetailView,
                            AnswerDeleteView,
                            AnswerUpdateView,
                            SearchAnswerView)

urlpatterns = [
    path('create_answer/', AnswerCreateView.as_view()),
    path('answer_list/', AnswersListView.as_view()),
    path('answer_list/<int:id>/', AnswerDetailView.as_view()),
    path('answer_list/<int:id>/delete/', AnswerDeleteView.as_view()),
    path('answer_list/<int:id>/update/', AnswerUpdateView.as_view()),
    path('search/', SearchAnswerView.as_view(), name='search')
]
