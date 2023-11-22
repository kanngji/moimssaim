import statistics
from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


app_name='promotion'

urlpatterns = [
    path('',views.promotion_list,name='promotion_list'),
    path('<int:promotion_id>/',views.promotion_detail,name='promotion_detail'),
    path('create/',views.promotion_create,name='promotion_create'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)