# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0003_auto_20170228_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='..{}img/dashboard/default-header.jpg', upload_to='image/', verbose_name='image'),
        ),
    ]