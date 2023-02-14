from django.urls import path 
from .views import AuthorAPI

urlpatterns = [ 
    path('api',AuthorAPI.as_view(),name='student'),
    #path('api/<int:pk>/',StudentDetail.as_view(),name='studentdetail'),

]
