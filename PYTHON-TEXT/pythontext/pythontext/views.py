# create file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('''<h1>welcome to ankercloud <h1> <a
    href="https://www.ankercloud.com"> Homepage </a>''')

def about(request):
    return HttpResponse('''<h1> About us <h1> <a
    href = "https://www.ankercloud.com/about"> click here  </a>''')

# def index(request):
#     return render(request, 'index.html')
#     # return HttpResponse("Home")
#
# def removepunc(request):
#     return HttpResponse("removepunc  <a href='/'>back></a>")
#
# def capfirst(request):
#     return HttpResponse("Capital first letter  <a href='/'>back></a>")
#
# def newlineremover(request):
#     return HttpResponse("new line remover   <a href='/'>back></a>")
# def spaceremove(request):
#     return HttpResponse("remove space  <a href='/'>back></a>")
