# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='code',
            new_name='dept_code',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='id',
            new_name='dept_id',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='name',
            new_name='dept_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='addr',
            new_name='per_addr',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='code',
            new_name='per_code',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='email',
            new_name='per_email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='id',
            new_name='per_id',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='per_name',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='addr',
            new_name='sub_addr',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='code',
            new_name='sub_code',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='id',
            new_name='sub_id',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='name',
            new_name='sub_name',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='addr',
            new_name='per_addr',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='code',
            new_name='per_code',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='email',
            new_name='per_email',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='id',
            new_name='per_id',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='name',
            new_name='per_name',
        ),
    ]
