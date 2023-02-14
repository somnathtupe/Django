from django.shortcuts import render
from .models import News 


def index(request):
    context = {'file':News.objects.all()}
    return render(request,"index.html",context)

def index1(request):
    if request.method =='POST':
        title = request.POST['title']
        desc= request.POST['desc']
        upload1=request.FILES['upload']
        object=News.objects.create(title=title,desc=desc,upload=upload1)
        object.save()

    context = News.objects.all()
    return render(request,'index1.html',{'context':context})
