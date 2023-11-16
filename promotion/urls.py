from django.urls import path
from . import views

app_name='promotion'

urlpatterns = [
    path('',views.promotion_list,name='promotion_list'),
    # path('<int:promotion_id>/',views.promotion_detail,name='promotion_detail'),
    path('create/',views.promotion_create,name='promotion_create'),
]