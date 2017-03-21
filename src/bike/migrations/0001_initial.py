# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 23:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geo', '0003_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name': 'Edition',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('category', models.CharField(choices=[('Car', 'Car'), ('Motorcycle', 'Motorcycles'), ('Vehicle', 'Vehicle')], max_length=100, verbose_name='Category')),
                ('price', models.IntegerField(default=0)),
                ('negotiable', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50)),
                ('condition', models.CharField(choices=[('NEW', 'New'), ('OLD', 'Old')], max_length=50, verbose_name='Condition')),
                ('seller_type', models.CharField(choices=[('DEALER', 'Dealer'), ('PRIVATE', 'Private')], max_length=50, verbose_name='Seller Type')),
                ('fuel', models.CharField(choices=[('DIESEL', 'Diesel'), ('ELECTRO', 'Electro'), ('GASOLINE', 'Gasoline')], max_length=50, verbose_name='Fuel')),
                ('transmission', models.CharField(choices=[('AUTOMATIC', 'Automatic'), ('MANUAL', 'Manual')], max_length=50, verbose_name='Transmission')),
                ('lifestyle', models.CharField(choices=[('FAMILY', 'Family'), ('LUXURY', 'Luxury'), ('OFFROAD', 'Offroad'), ('CLASSIC', 'Classic')], max_length=50, verbose_name='Lifestyle')),
                ('color_family', models.CharField(choices=[('WHITE', 'White'), ('BLACK', 'Black')], max_length=50, verbose_name='Color Family')),
                ('details', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('submitted_on', models.DateField(auto_now=True, verbose_name='Submitted on')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike.Brand', verbose_name='Brand')),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike.Edition', verbose_name='Edition')),
                ('locations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.Region', verbose_name='Locations')),
                ('posted_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-submitted_on'],
                'db_table': 'bike',
                'verbose_name': 'Item',
            },
        ),
    ]
