from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login

from .forms import UserForm

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
    