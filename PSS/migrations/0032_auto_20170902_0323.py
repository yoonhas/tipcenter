# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-02 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PSS', '0031_surveytimes_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyee',
            name='survey1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='surveyee',
            name='survey2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='surveyee',
            name='survey3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='surveyee',
            name='survey4',
            field=models.BooleanField(default=False),
        ),
    ]
