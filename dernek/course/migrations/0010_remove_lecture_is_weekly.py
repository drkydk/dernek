# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 08:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_lecture_is_weekly'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='is_weekly',
        ),
    ]
