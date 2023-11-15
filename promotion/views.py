from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
# Create your views here.

@api_view(['GET','POST'])
def promotion_list(request):
    return render(request,'promotion/promotion_list.html')
