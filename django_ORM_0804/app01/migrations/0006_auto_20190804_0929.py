# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-04 09:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_book_athuor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='athuor',
            new_name='author',
        ),
    ]