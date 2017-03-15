# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geo', '0003_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('location', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='geo.Region')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]