from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

#creating router object
router=DefaultRouter()

#Register StudentViewSet with Router
 
router.register('studentapi',views.StudentModelViewSet,basename='student')
#use sudo lsof -t -i tcp:8000 | xargs kill -9 to kill the error port is already in use for ubantu
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))

]