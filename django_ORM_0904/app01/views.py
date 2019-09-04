from django.shortcuts import render

# Create your views here.
from app01.models import *
def index(req):
    # 方法一
    # b = Book(name="python基礎", price=99, author="alex", pub_date="2019-08-04")
    # b.save()
    # 方法二
    # Book.objects.create(name="MySQL", price=299, authors="alex", pub_date="2019-08-07",publish_id=2)
    # Book.objects.create(name="Go", price=2991, author="alex", pub_date="2019-08-07",publish_id=2)
    # Book.objects.create(name="py", price=199, author="alex", pub_date="2019-08-07",publish_id=1)
    # Author.objects.create(name="leon2", age=30)
    # Author.objects.create(name="kenson2")
    b_obj = Book.objects.all()
    print(b_obj)
    au_obj = Author.objects.get(id=2)
    print(au_obj)
    sample_object = Book.objects.create()
    sample_object.Book = [1, 2]
    return render(req,'index.html',locals())