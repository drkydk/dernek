# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 08:55
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_lecture_lecturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='color',
            field=colorfield.fields.ColorField(default='#FFF', max_length=10),
        ),
    ]