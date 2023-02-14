from django.contrib import admin
from newsapp.models import News

admin.site.register(News) 


display_list = ['title','news_desc']