# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-30 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PSS', '0045_auto_20180130_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveytimes',
            name='survey_kind',
        ),
        migrations.AddField(
            model_name='surveyee',
            name='survey_kind',
            field=models.IntegerField(default=1),
        ),
    ]
