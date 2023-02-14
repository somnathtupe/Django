
from django.urls import path 
from .views import StudentAPI,StudentDetail

urlpatterns = [ 
    path('api',StudentAPI.as_view(),name='student'),
    path('api/<int:pk>/',StudentDetail.as_view(),name='studentdetail'),

]
