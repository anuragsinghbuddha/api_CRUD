
from .models import student 
from .serializers import StudentSerializers
from rest_framework.generics import GenericAPIView 
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework import status 

#List and create are of same grp as they donot required pk
class studentList_Create(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=student.objects.all() 
    serializer_class=StudentSerializers 

    def get(self,requests,*args,**kwargs):
        return self.list(requests,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# to retrive,update,delete specific data from database as they required pk
class studentUpdate_destroy_retrive(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=student.objects.all() 
    serializer_class=StudentSerializers 

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
