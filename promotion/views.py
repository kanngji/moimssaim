from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from .models import Post
# Create your views here.

@api_view(['GET','POST'])
def promotion_list(request):
    promotion_list = Post.objects.order_by('-create_date')
    context = {'promotion_list':promotion_list}
    return render(request,'promotion/promotion_list.html',context)


