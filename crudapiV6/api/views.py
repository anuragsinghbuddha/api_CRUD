
from .models import student 
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status 

#List and create are of same grp as they donot required pk
class studentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu=student.objects.all() 
        serializer=StudentSerializers(stu,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        id=pk 
        if pk is not None:
            stu=student.objects.get(id=id)
            serializer=StudentSerializers(stu)
            return Response(serializer.data)



    def create(self, request):
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)
        
    
    def update(self,requests,pk):
        id=pk 
        if id is not None:
            stu=student.objects.get(pk=id)
            serializer=StudentSerializers(stu,data=requests.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data partial Updated'})
        return Response(serializer.errors)

    def partial_update(self,requests,pk):
        id=pk 
        if id is not None:
            stu=student.objects.get(pk=id)
            serializer=StudentSerializers(stu,data=requests.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated'})
            return Response(serializer.errors)
        


    def destroy(self,requests,pk):
        id=pk 
        
        stu=student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})