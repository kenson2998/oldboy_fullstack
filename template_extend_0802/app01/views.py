from django.shortcuts import render


# Create your views here.

def backend(request):
    return render(request, "base.html")
def student(request):
    student_list = ["Leon","Leo","Leona"]
    return render(request, "student.html",locals())
