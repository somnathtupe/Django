from django.shortcuts import render
from django.http import Http404
from .models import  Student
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from .seriallizers import StudentSerializer 

class StudentAPI(APIView):
    def get(self,request):
      stu = Student.objects.all()
      serializer = StudentSerializer(stu,many=True)
      return Response(serializer.data)

    def post(self,request): 
        data = request.data 
        serializer = StudentSerializer(data=data,many=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
        snippet = Student.objects.all()
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class StudentDetail(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(sid=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StudentSerializer(snippet)
        #print(snippet.name)
        #return Response(snippet.name)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StudentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   

