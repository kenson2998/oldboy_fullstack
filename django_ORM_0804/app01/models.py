from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateField()
    author = models.CharField(max_length=32, null=False)
    publish = models.ForeignKey("publish")

class publish(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

class Author(models.Model):
    name = models.CharField(max_length=20)

