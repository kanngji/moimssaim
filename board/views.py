import json
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Question, Answer
from django.shortcuts import render, get_object_or_404,redirect, resolve_url
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def board_list(request):
    page = request.GET.get('page','1') # 페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list,10) # 페이지당 10개 씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list':page_obj}
    return Response(context, template_name='board/question_list.html')

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def board_detail(request,question_id):
    try:
        question = Question.objects.get(id=question_id)
        context={'question':question}
        return Response(context,template_name='board/question_detail.html')
    except Question.DoesNotExist:
        return Response(template_name='404.html')
    
@api_view(['POST'])
@renderer_classes([TemplateHTMLRenderer])
def answer_create(request,question_id):
    question = Question.objects.get(id=question_id)
    if request.method =="POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            if request.user.is_authenticated:
                answer.author = request.user # author속성에 로그인계정 저장
            else:
                nonregisteruser, create = User.objects.get_or_create(username='비회원')
                answer.author=nonregisteruser
            
            answer.create_date=timezone.now()
            answer.question = question
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('board:board_detail', question_id=question.id), answer.id))
    else:
        return Response(template_name='404.html')
    
    context={'question':question, 'form':form}
    return Response(context,template_name='board/question_detail.html')
    # try:
    #     question = Question.objects.get(id=question_id)
    #     answer = Answer(question=question, content=request.POST.get('content',''), create_date=timezone.now())
    #     answer.save()
    #     return redirect('board:board_detail',question_id=question.id)
    # except Question.DoesNotExist:
    #     return Response(template_name='404.html')
    
@api_view(['GET','POST'])
@renderer_classes([TemplateHTMLRenderer])
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            if request.user.is_authenticated:
                question.author = request.user # author 속성에 로그인계정 저장
            else:
                noregisteruser, created = User.objects.get_or_create(username='비회원')
                question.author = noregisteruser

            
            question.create_date=timezone.now()
            question.save()
            return redirect('board:board_list')
    else:
        form = QuestionForm()
    context={'form':form}
    return Response(context,template_name='board/question_form.html')

@api_view(['GET','POST'])
@renderer_classes([TemplateHTMLRenderer])
def question_modify(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    # if request.user != question.author:
    #     messages.error(request, '수정권한이 없습니다.')
    #     return redirect('board:board_detail', question_id=question.id)
    
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date= timezone.now() #수정일시 저장
            question.save()
            return redirect('board:board_detail', question_id=question.id)    
    else:
        form = QuestionForm(instance = question)
    context = {'form':form}
    return render(request, 'board/question_form.html',context)

@api_view(['GET','POST'])
@renderer_classes([TemplateHTMLRenderer])
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('board:board_list')

@api_view(['GET','POST'])
@renderer_classes([TemplateHTMLRenderer])
def answer_modify(request,answer_id):
    answer = get_object_or_404(Answer,pk=answer_id)
    # if request.user != question.author:
    #     messages.error(request, '수정권한이 없습니다.')
    #     return redirect('board:board_detail', question_id=question.id)
    
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date= timezone.now() #수정일시 저장
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('board:board_detail', question_id=answer.question.id), answer.id))  
    else:
        form = AnswerForm(instance = answer)
    context = {'answer':answer,'form':form}
    return render(request, 'board/answer_form.html',context)

@api_view(['GET','POST'])
@renderer_classes([TemplateHTMLRenderer])
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()
    return redirect('board:board_detail', question_id=answer.question.id)


@api_view(["GET",'POST'])
@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    question.voter.add(request.user)
    return redirect('board:board_detail', question_id=question.id)

@login_required(login_url='common:login')
def answer_vote(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    
    answer.voter.add(request.user)
    return redirect('{}#answer_{}'.format(
                resolve_url('board:board_detail', question_id=answer.question.id), answer.id))