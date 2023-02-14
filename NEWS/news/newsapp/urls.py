from django.urls import path 
from . import views
from django.views.static import serve
from django.conf import settings


urlpatterns = [
                path('',views.index,name='index'),
                path('index1',views.index1,name='index1'),
                path(r'^download/(?p<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})
]
