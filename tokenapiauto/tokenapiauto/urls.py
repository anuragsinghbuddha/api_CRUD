"""tokenauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
#creating router object
router=DefaultRouter()
#from rest_framework.authtoken.views import obtain_auth_token
#Register StudentViewSet http://ai.gov.in/with Router
 
router.register('studentapi',views.StudentModelViewSet,basename='student')
#use sudo lsof -t -i thttp://ai.gov.in/cp:8000 | xargs kill -9 to kill the error port is already in use for ubantu
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
    # use this command in terminal to get api key -http POST http://127.0.0.1:8000/gettoken/ username="anurag" password="anurag"
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))

]