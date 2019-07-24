from django.shortcuts import render, HttpResponse
import time


# Create your views here.

# request 就是封裝成一個對象
# 處理完以後要打包response發回去前端

def show_time(request):  # 必須要有req行參 ,給 user傳輸的
    times = time.ctime()
    # return HttpResponse("Hello")
    # return render(request, "show_timea.html", locals())
    return render(request, "show_timea.html", {"times": times})
