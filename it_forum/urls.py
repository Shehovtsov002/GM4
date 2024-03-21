from django.urls import path
from it_forum.views import (create_answer_it_forum_view,
                            answer_list_it_forum_view,
                            answer_detail_it_forum_view,
                            delete_answer_it_forum_view,
                            update_answer_it_forum_view)

urlpatterns = [
    path('create_answer/', create_answer_it_forum_view),
    path('answer_list/', answer_list_it_forum_view),
    path('answer_list/<int:answer_id>/', answer_detail_it_forum_view),
    path('answer_list/<int:answer_id>/delete/', delete_answer_it_forum_view),
    path('answer_list/<int:answer_id>/update/', update_answer_it_forum_view),
]
