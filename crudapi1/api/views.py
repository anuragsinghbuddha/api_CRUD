from django.shortcuts import render
import io
from .models import Student
from rest_framework.parsers import JSONParser 
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def student_api(request):
    if request.method =='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)        
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializers(stu)
        
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu=Student.objects.all()
        serializer=StudentSerializers(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    if request.method =='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)        
        pythondata=JSONParser().parse(stream) 
        serializer=StudentSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Successfully Inserted'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    if request.method =='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)        
        pythondata=JSONParser().parse(stream) 
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializers(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data successfully Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)        
        pythondata=JSONParser().parse(stream) 
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'Data successfully deleted'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
    json_data=JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data,content_type='application/json')



