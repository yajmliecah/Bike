# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-04 16:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0004_category_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]
