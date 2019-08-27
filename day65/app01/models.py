from django.db import models


# Create your models here.

class Class(models.Model):
    title = models.CharField(max_length=20)


class student(models.Model):
    name = models.CharField(max_length=20)
    class_id = models.ForeignKey(Class)

    def __str__(self):
        return self.name


class teacher(models.Model):
    name = models.CharField(max_length=20)
