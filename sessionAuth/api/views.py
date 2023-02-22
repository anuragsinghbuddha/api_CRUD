
from .models import student 
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions

# WE CAN AUTHENTICATE IN BOTH WAY if we will write in class it is locallily authenticated and for globally autenticatd go and see in setting
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=StudentSerializers
    authentication_classes=[SessionAuthentication]
    #permission_classes=[IsAuthenticated]
    #permission_classes=[IsAdminUser]
    #permission_classes=[AllowAny]
    #permission_classes=[IsAuthenticatedOrReadOnly]
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]

