# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-10 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0015_auto_20171010_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='short_desc',
            field=models.CharField(default='Shortened Description for Product', max_length=350, verbose_name='Short Description'),
        ),
        migrations.AddField(
            model_name='item',
            name='view',
            field=models.BooleanField(default=0),
        ),
    ]
