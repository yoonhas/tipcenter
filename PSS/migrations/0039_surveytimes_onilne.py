# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-22 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PSS', '0038_auto_20180108_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveytimes',
            name='onilne',
            field=models.BooleanField(default=False),
        ),
    ]