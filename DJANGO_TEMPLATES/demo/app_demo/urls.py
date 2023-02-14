
from . import views
from django.urls import path

urlpatterns = [
             path('', views.Course, name='home-page'),
             path('<int:course_id>/', views.details, name='details'),

]