# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-02 10:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='City')),
                ('desc', models.CharField(max_length=200, verbose_name='City description')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'City',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Organization name')),
                ('desc', models.TextField(verbose_name='Organization description')),
                ('click_nums', models.IntegerField(default=0, verbose_name='Click times')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='Favorite times')),
                ('image', models.ImageField(upload_to='org/%Y/%m', verbose_name='Cover')),
                ('address', models.CharField(max_length=150, verbose_name='Organization address')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CityDict', verbose_name='Location')),
            ],
            options={
                'verbose_name': 'Course provider',
                'verbose_name_plural': 'Course provider',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Teacher name')),
                ('work_years', models.IntegerField(default=0, verbose_name='Work times')),
                ('work_company', models.CharField(max_length=50, verbose_name='Work company')),
                ('work_position', models.CharField(max_length=50, verbose_name='Work position')),
                ('points', models.CharField(max_length=50, verbose_name='Teaching characteristics')),
                ('click_nums', models.IntegerField(default=0, verbose_name='Click times')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='Favorite times')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='Subsidiary organ')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teacher',
            },
        ),
    ]
