from django.shortcuts import render
from .serializer import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.
def student_info(request,pk):
    stu= Student.objects.get(id=pk)
    print("-------------")
    print(stu)
    serializer=StudentSerializer(stu)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data)
    return JsonResponse(serializer.data)

def student(request):
    stu= Student.objects.all()
    print("-------------")
    print(stu)
    serializer=StudentSerializer(stu, many=True)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data)
    return JsonResponse(serializer.data, safe=False)