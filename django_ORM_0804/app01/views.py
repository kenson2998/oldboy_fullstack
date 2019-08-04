from django.shortcuts import render, HttpResponse
from app01.models import *


# Create your views here.


def index(requests):
    return render(requests, "index.html")


def addbook(requests):
    # 方法一
    # b = Book(name="python基礎", price=99, author="alex", pub_date="2019-08-04")
    # b.save()
    # 方法二
    Book.objects.create(name="Linux", price=199, author="alex3", pub_date="2019-08-04")

    return HttpResponse("新增成功!")


def updatebook(requests):
    # Book.objects.filter(author="alex").update(price=99)
    b = Book.objects.get(author="alex")
    print(b)
    b.price = 100
    b.save()
    print(type(b))

    return HttpResponse("修改成功!")


def delbook(requests):
    Book.objects.filter(author="alex3").delete()

    return HttpResponse("刪除成功!")


def md5(request, x1):
    import hashlib
    # m = hashlib.md5()
    # m.update(x.encode())
    # x1 = m.hexdigest()
    # print(2,x1)  # hex格式加密



    enc = [
        'f2b1fa56c4754138166eab02d0646113',
        'd8f7de479b1fae3d85d341f380524de5',
        '5c443b2003676fa5e8966030ce3a86ea',
        '4637c746b772dac729a80c93861521c1',
    ]

    if x1 in enc:
        return HttpResponse("password 正確")
    # m.update(b'Its me')
    # print(m.hexdigest())
    # m.update(b'Its too long to buy something')
    # print(m.hexdigest())
    #
    # m2 = hashlib.md5()
    # m2.update(b'HelloIts me')  # 中間沒空格 但md5加密後的值卻相同
    # print(m2.hexdigest())
    #
    # s2 = hashlib.sha1()
    # s2.update(b'HelloIts me')
    # print(s2.hexdigest())

    # import hmac  # 用於訊息加密
    #
    # h = hmac.new(b'sky king against tiger', b'you are 250')
    #
    # print(h.digest())
    # print(h.hexdigest())

    return HttpResponse("密碼失敗")


def md5_name(request,x2):
    import hashlib
    m = hashlib.md5()
    m.update(x2.encode())
    x1 = m.hexdigest()
    print(2,x1)  # hex格式加密
    return HttpResponse(x2+"你的密碼是："+x1+"<a href='/md5/"+x1+"'>點擊驗證</a>")
