from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from .models import Allcourses
from django.template import loader


def Course(request):
    ac = Allcourses.objects.all()
    template = loader.get_template('course.html')
    context = {
        'ac':ac,
    }
    return HttpResponse(template.render(context,request))

def details(request,course_id):
    try:
        course = Allcourses.objects.get(pk=course_id)
    except Allcourses.DoesNotExits:
        raise Http404('<h1>Page not found</h1>')
    else:
        return render(request, 'details.html', {'course': course})
