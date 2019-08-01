from django.shortcuts import render, HttpResponse
import time, datetime


# Create your views here.
def show_time(request):
    t = datetime.datetime.now()
    va = f"<p> it is {t}</p>"
    return HttpResponse(va)


def index1(request):
    return render(request, 'index2.html')


def login(request):
    return render(request, "index.html")


def tag(request):
    return render(request, 'mytag.html', {"t": 5})
