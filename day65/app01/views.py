from django.shortcuts import render
from app01.models import *

# Create your views here.

def classes(request):
    class_list = Class.objects.all().values()
    return render(request, 'classes.html',locals())


def students(request):
    '''
    學生列表
    :param request: 封裝請求相關所有信息
    :return:
    '''
    stu = student.objects.all().values()
    return render(request,'students.html',locals())