
from .models import student 
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.response import Response


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=StudentSerializers