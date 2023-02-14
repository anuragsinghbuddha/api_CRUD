
from .models import student 
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.response import Response


class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=student.objects.all()
    serializer_class=StudentSerializers