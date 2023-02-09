from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import student 
from .serializers import StudentSerializers
from rest_framework import status

class studentApi(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:  
            stu=student.objects.get(pk=id)
            serializer=StudentSerializers(stu)
            return Response(serializer.data)    
        id=request.data.get(id)

        stu=student.objects.all()
        serializer=StudentSerializers(stu,many=True)
        return Response(serializer.data)


    def post(self,request,format=None):
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"data is saved"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None,format=None):
        id=pk
        stu=student.objects.get(pk=id)   
        serializer=StudentSerializers(stu,data=request.data)    
        if serializer.is_valid():
            serializer.save()   
            return Response({'msg':'Complete Data Updated'})        
        return Response(serializer.errors) 

    def patch(self,request,pk=None,format=None):
        id=pk
        stu=student.objects.get(pk=id)   
        serializer=StudentSerializers(stu,data=request.data,partial=True)    
        if serializer.is_valid():
            serializer.save()   
            return Response({'msg':'Partial Data Updated'})        
        return Response(serializer.errors)


    def delete(self,request,pk=None,format=None):
        id=pk
        stu=student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'}) 




  