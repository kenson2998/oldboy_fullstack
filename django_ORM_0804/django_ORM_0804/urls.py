"""django_ORM_0804 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', views.index),
    url(r'^addbook/', views.addbook),
    url(r'^updatebook/', views.updatebook),
    url(r'^delbook/', views.delbook),
    url(r'^md5/([a-zA-Z0-9]{32})', views.md5),
    url(r'^md5_name/([a-zA-Z0-9]{0,10})', views.md5_name),

]
