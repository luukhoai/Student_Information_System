# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('middle_score', models.FloatField(default=0)),
                ('final_score', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.PositiveIntegerField(unique=True)),
                ('addr', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('joined_date', models.DateField()),
                ('average_score', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.PositiveIntegerField(unique=True)),
                ('addr', models.CharField(max_length=100)),
                ('department', models.ForeignKey(to='students.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.PositiveIntegerField(unique=True)),
                ('addr', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('joined_date', models.DateField()),
                ('salary', models.PositiveIntegerField(default=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(to='students.Teacher'),
        ),
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(related_name='students_student_related', through='students.Score', to='students.Subject'),
        ),
        migrations.AddField(
            model_name='score',
            name='student',
            field=models.ForeignKey(to='students.Student'),
        ),
        migrations.AddField(
            model_name='score',
            name='subject',
            field=models.ForeignKey(to='students.Subject'),
        ),
    ]
