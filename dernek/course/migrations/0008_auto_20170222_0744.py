# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 07:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20170222_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='day',
        ),
        migrations.AddField(
            model_name='lecture',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 2, 22, 7, 44, 46, 444313, tzinfo=utc), verbose_name='tarih'),
            preserve_default=False,
        ),
    ]
