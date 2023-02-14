from django.shortcuts import render
from bookapp.models import Book,Cart




def index(request):

   context = Book.objects.all()
   return render(request,'index.html',{'book':context})

