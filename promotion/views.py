from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from .models import Post
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .forms import PostForm
# Create your views here.

@api_view(['GET','POST'])
def promotion_list(request):
    promotion_list = Post.objects.order_by('-create_date')
    context = {'promotion_list':promotion_list}
    return render(request,'promotion/promotion_list.html',context)


@api_view(['GET',"POST"])
@renderer_classes([TemplateHTMLRenderer])
def promotion_detail(request,promotion_id):
    try:
        promotion = Post.objects.get(id=promotion_id)
        context ={'promotion':promotion}
    except Post.DoesNotExist:
        return Response(template_name='404.html')
    return render(request,'promotion/promotion_detail.html',context)

@api_view(["GET","POST"])
def promotion_create(request):
    form = PostForm()
    return render(request, 'promotion/post_form.html',{'form':form})