# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 08:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0010_remove_lecture_is_weekly'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='lecturer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='eğitmen'),
            preserve_default=False,
        ),
    ]
