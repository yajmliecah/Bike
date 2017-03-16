# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170316_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikeuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bikeuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]