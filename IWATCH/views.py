from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from django.contrib.auth.models import User
from board.models import Question 
from promotion.models import Post

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def home(request):
    # 총 회원 가입한 수
    total_users = User.objects.count()
    # 총 BOARD QUESTION 수
    total_questions = Question.objects.count()
    # 총 PROMOTION POST 수
    total_posts = Post.objects.count()
    context={
        'total_users':total_users,
        'total_questions':total_questions,
        'total_posts':total_posts,

    }
    return render(request,'home.html',context)