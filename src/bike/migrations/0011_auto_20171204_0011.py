# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-04 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0010_auto_20171027_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
