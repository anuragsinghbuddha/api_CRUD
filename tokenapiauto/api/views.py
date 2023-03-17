
from .models import student 
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class StudentModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=student.objects.all()
    serializer_class=StudentSerializers
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]