# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0003_region'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Region',
            new_name='City',
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['-name'], 'verbose_name': 'Countrie'},
        ),
    ]
