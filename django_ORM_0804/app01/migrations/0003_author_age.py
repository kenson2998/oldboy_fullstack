# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-04 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
