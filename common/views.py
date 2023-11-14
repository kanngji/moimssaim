from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import UserForm, UserInfoForm
from .models import Info

# Create your views here.
@api_view(['GET','POST'])
@renderer_classes([TemplateHTMLRenderer])
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserForm()
    return Response({'form':form},template_name='common/signup.html')

@api_view(['GET','POST'])
@login_required(login_url='common:login')
def myinfo(request):
    try:
        myinfo = Info.objects.get(user=request.user)
    except Info.DoesNotExist:
        myinfo = None
        
    if request.method=="POST":
        form = UserInfoForm(request.POST,instance=myinfo)
        if form.is_valid():
            myinfo = form.save(commit=False)
            myinfo.user = request.user
            myinfo.save()
            return redirect('common:myinfo')
    else:
        form = UserInfoForm(instance=myinfo)
    context={'form':form}
    return render(request, 'common/myinfo_form.html',context)