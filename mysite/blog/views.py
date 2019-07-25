from django.shortcuts import render, HttpResponse, render_to_response
import time


# Create your views here.

# request 就是封裝成一個對象
# 處理完以後要打包response發回去前端

def show_time(request):  # 必須要有req行參 ,給 user傳輸的
    times = time.ctime()
    # return HttpResponse("Hello")
    # return render(request, "show_timea.html", locals())
    return render(request, "show_timea.html", locals())


def article_year(request, year,month):
    return HttpResponse(year)


def article_year_month(request, year, month):
    return HttpResponse(year + month)


def number(request, num, year):
    listq = {"2212": "Leon", "2215": "Mario", "2213": "艾力克斯"}
    list_year = {"2019": "技術部組長", "2018": "Gary愛將"}
    return HttpResponse(listq[num] + "是" + list_year[year])


def register(request):
    print("return url_path:", request.path)
    print("return url_path:", request.get_full_path())

    if request.method == "POST":
        print(request.POST.get("user"))
        return HttpResponse("success!")
    return render(request, "register.html", locals())

def login(request):
    if request.method == "POST":
        print(request.POST.get('user'))
        return HttpResponse("Leon 登錄")
    return render(request,"login.html",locals())