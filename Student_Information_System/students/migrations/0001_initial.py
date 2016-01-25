# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('joined_date', models.DateField()),
                ('average_score', models.FloatField()),
                ('email', models.EmailField(default=b'user@gmail.com', max_length=254)),
            ],
            options={
                'ordering': ['-joined_date'],
            },
        ),
        migrations.AddField(
            model_name='classroom',
            name='course',
            field=models.ForeignKey(to='students.Course'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='student',
            field=models.ManyToManyField(to='students.Student'),
        ),
    ]
