# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_lecture_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='students',
        ),
        migrations.AddField(
            model_name='lecture',
            name='students',
            field=models.TextField(default=0, verbose_name='öğrenciler'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
