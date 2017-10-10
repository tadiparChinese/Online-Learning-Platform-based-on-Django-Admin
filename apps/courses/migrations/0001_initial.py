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
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Course name')),
                ('desc', models.CharField(max_length=300, verbose_name='Course description')),
                ('detail', models.TextField(verbose_name='Course detail')),
                ('degree', models.CharField(choices=[('cj', 'Begining level'), ('zj', 'Middle level'), ('gj', 'High level')], max_length=2)),
                ('learn_times', models.IntegerField(default=0, verbose_name='Learning time(In minutes)')),
                ('students', models.IntegerField(default=0, verbose_name='Total enrolled students')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='Favorite number')),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='Cover')),
                ('click_num', models.IntegerField(default=0, verbose_name='Click times')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add time')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Course',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('download', models.FileField(upload_to='course/resource/%Y/%m', verbose_name='Resource files')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add time')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Course resources',
                'verbose_name_plural': 'Course resources',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Chapter name')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add time')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Chapter',
                'verbose_name_plural': 'Chapter',
            },
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Video name')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add time')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='Chapter')),
            ],
            options={
                'verbose_name': 'Course video',
                'verbose_name_plural': 'Course video',
            },
        ),
    ]
