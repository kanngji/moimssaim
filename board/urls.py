from django.urls import path
from . import views


app_name='board'


urlpatterns = [
    path('', views.board_list,name='board_list'),
    path('<int:question_id>/',views.board_detail,name='board_detail'),
    path('answer/create/<int:question_id>/',views.answer_create, name='answer_create'),
    path('question/create/',views.question_create, name='question_create'),
    path('quesiton/modify/<int:question_id>/',views.question_modify,name='question_modify'),
    path('question/delete/<int:question_id>/',views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>', views.answer_modify,name='answer_modify'),
    path('answer/delete/<int:answer_id>/',views.answer_delete,name='answer_delete'),
    path('question/vote/<int:question_id>/',views.question_vote,name='question_vote'),
    path('answer/vote/<int:answer_id>/', views.answer_vote, name='answer_vote'),

]