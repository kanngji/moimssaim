from datetime import timezone , datetime
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view, renderer_classes
from .models import Post
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .forms import PostForm
from django.http import JsonResponse
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
        data = {
            'title':promotion.title,
            'discription':promotion.discription,
            'category':promotion.category,
            'meet_date':promotion.meet_date,
            
        }
    except Post.DoesNotExist:
        return Response(template_name='404.html')
    return JsonResponse(data)

@api_view(["GET","POST"])
def promotion_create(request):
    if request.method=="POST":
        # form = PostForm(request.POST,request.FILES)
        # if form.is_valid():
        #     post = form.save(commit=False)
        #     post.create_date=datetime.now()
        #     post.save()
        #     return redirect('promotion:promotion_list')
        post = Post()
        post.title=request.POST['title']
        post.discription=request.POST['discription']
        post.create_date=datetime.now()
        post.meet_date=request.POST['meet_date']
        post.category=request.POST['category']
        post.imgfile=request.FILES['imgfile']
        post.save()
        return redirect('promotion:promotion_list')
    else:
        form = PostForm()
    context={'form':form}
    return render(request, 'promotion/post_form.html',context)