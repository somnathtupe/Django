from django.shortcuts import render

from django.shortcuts import render
from django.http import Http404,JsonResponse 
from .models import  Author
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from .seriallizers import AuthorSerializer 

class AuthorAPI(APIView):
    def get(self,request):
      stu = Author.objects.all()
      serializer = AuthorSerializer(stu,many=True)
      return Response(serializer.data)
      #return JsonResponse(serializer.data,safe=False)

    def post(self,request): 
        data = request.data 
        serializer = AuthorSerializer(data=data,many=True)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #     res={'msg':'Data Has been Created Successfully'}
        #     return Response(res,status=status.HTTP_201_CREATED)

        # return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    # def delete(self,request):
    #     stu = request.data 
    #     id = stu.get('id')
    #     stu = Student.objects.get(id=id)
    #     stu.delete()
    #     # res={'msg':'Student deleted Successfully'}
    #     # return Response(res) 
    #     return Response(status=status.HTTP_202_ACCEPTED)

    def delete(self,request,format=None):
        snippet = Author.objects.all()
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

