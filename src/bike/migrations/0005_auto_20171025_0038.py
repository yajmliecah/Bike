# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-25 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0004_subcategory_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ManyToManyField(null=True, to='bike.Category', verbose_name='Categories'),
        ),
    ]
