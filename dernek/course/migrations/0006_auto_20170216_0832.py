# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 08:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20170216_0824'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classroom',
            options={'verbose_name': 'Derslik', 'verbose_name_plural': 'Derslikler'},
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='lecture_per_day',
        ),
        migrations.AddField(
            model_name='classroom',
            name='quota',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecture',
            name='classroom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.Classroom', verbose_name='derslik'),
            preserve_default=False,
        ),
    ]
